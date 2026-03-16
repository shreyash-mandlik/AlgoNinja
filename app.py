import streamlit as st
import time
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from algorithms_data import algorithms, complexity_data, interview_questions
import streamlit.components.v1 as components

# ================================
# Page Config
# ================================
st.set_page_config(
    page_title="AlgoNinja 🥷",
    page_icon="🥷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ================================
# Custom CSS
# ================================
st.markdown("""
<style>
    .ninja-header {
        text-align: center;
        padding: 1rem;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# ================================
# Sidebar
# ================================
st.sidebar.markdown("# 🥷 AlgoNinja")
st.sidebar.markdown("*Master algorithms like a ninja!*")
st.sidebar.divider()

page = st.sidebar.radio("Navigate", [
    "🏠 Home",
    "📚 Learn Algorithms",
    "⚡ Algorithm Race",
    "📊 Complexity Table",
    "🧩 Quiz Mode",
    "🎯 Interview Prep",
    "🔍 Search Algorithm"
])

# ================================
# HOME PAGE
# ================================
if page == "🏠 Home":
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h1 style='font-size: 60px;'>🥷 AlgoNinja</h1>
        <h3 style='color: #888;'>Master algorithms like a ninja!</h3>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📚 Algorithms", "18+")
    with col2:
        st.metric("💻 Languages", "4")
    with col3:
        total_q = sum(len(a['quiz'])
                      for cat in algorithms.values()
                      for a in cat.values())
        st.metric("🧩 Quiz and Intrview Questions", f"{total_q}+")
    with col4:
        st.metric("📊 Categories", len(algorithms))

    st.divider()
    st.subheader("📚 Algorithm Categories")

    cols = st.columns(3)
    cat_icons = {
        "Search Algorithms": "🔍",
        "Sorting Algorithms": "🔢",
        "Graph Algorithms": "🗺️",
        "Dynamic Programming": "⚡",
        "Game Algorithms": "🎮",
        "Intelligent Agents": "🤖"
    }

    for i, (cat, algos) in enumerate(algorithms.items()):
        with cols[i % 3]:
            icon = cat_icons.get(cat, "📌")
            algo_names = ", ".join(algos.keys())
            st.info(f"{icon} **{cat}**\n\n{algo_names}")

    st.divider()
    st.subheader("🚀 How to use AlgoNinja")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        1. **📚 Learn** → Pick any algorithm
        2. **💻 Choose language** → Python, C++, Java, JS
        3. **🎬 Step through** → Walk through step by step
        4. **🧩 Quiz** → Test your understanding
        """)
    with col2:
        st.markdown("""
        5. **⚡ Race** → Compare algorithm speeds
        6. **📊 Complexity** → Big O comparison
        7. **🎯 Interview** → Practice real questions
        8. **🔍 Search** → Find any algorithm fast
        """)

# ================================
# LEARN ALGORITHMS PAGE
# ================================
elif page == "📚 Learn Algorithms":
    st.title("📚 Learn Algorithms")

    col1, col2 = st.columns([1, 3])

    with col1:
        category = st.selectbox("Category", list(algorithms.keys()))
        algo_name = st.selectbox("Algorithm",
                                  list(algorithms[category].keys()))
        language = st.selectbox("Language",
                                 ["Python", "C++", "Java", "JavaScript"])

    algo = algorithms[category][algo_name]

    with col2:
        diff_color = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
        st.markdown(f"## {algo['full_name']}")
        st.markdown(
            f"{diff_color.get(algo['difficulty'], '⚪')} "
            f"**{algo['difficulty']}** | "
            f"⏱️ {algo['time_complexity']} | "
            f"💾 {algo['space_complexity']}"
        )
        st.divider()

        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "📖 Theory", "📝 Pseudocode",
            "💻 Code", "🎬 Steps", "🧩 Quiz"])

        with tab1:
            st.markdown(algo['description'])
            col_a, col_b, col_c = st.columns(3)
            with col_a:
                st.metric("Best Case", algo['best_case'])
            with col_b:
                st.metric("Average", algo['time_complexity'])
            with col_c:
                st.metric("Space", algo['space_complexity'])

        with tab2:
            st.code(algo['pseudocode'], language='text')

        with tab3:
            st.code(algo['code'][language],
                    language=language.lower().replace('javascript', 'js').replace('c++', 'cpp'))
            st.success(f"✅ Showing {language} implementation")

        with tab4:
            st.subheader("Step by Step Walkthrough")

            # Interactive stepper
            step_key = f"step_{algo_name}"
            if step_key not in st.session_state:
                st.session_state[step_key] = 0

            total_steps = len(algo['steps'])
            current = st.session_state[step_key]

            st.info(f"**Step {current+1}/{total_steps}:** "
                    f"{algo['steps'][current]}")
            st.progress((current+1)/total_steps)

            col_prev, col_next, col_reset = st.columns(3)
            with col_prev:
                if st.button("⬅️ Previous", key=f"prev_{algo_name}"):
                    if st.session_state[step_key] > 0:
                        st.session_state[step_key] -= 1
                        st.rerun()
            with col_next:
                if st.button("➡️ Next", key=f"next_{algo_name}"):
                    if st.session_state[step_key] < total_steps-1:
                        st.session_state[step_key] += 1
                        st.rerun()
            with col_reset:
                if st.button("🔄 Reset", key=f"reset_{algo_name}"):
                    st.session_state[step_key] = 0
                    st.rerun()

            st.divider()
            st.subheader("All Steps:")
            for i, step in enumerate(algo['steps']):
                if i == current:
                    st.success(f"**→ Step {i+1}:** {step}")
                else:
                    st.markdown(f"Step {i+1}: {step}")

        with tab5:
            st.subheader(f"Quiz — {algo['full_name']}")

            answers = []
            for i, q in enumerate(algo['quiz']):
                st.markdown(f"**Q{i+1}: {q['question']}**")
                ans = st.radio("", q['options'],
                               key=f"quiz_{algo_name}_{i}",
                               index=None)
                answers.append((ans, q['answer']))
                st.divider()

            if st.button("Submit Quiz ✅",
                         type="primary",
                         key=f"submit_{algo_name}"):
                score = sum(1 for ans, correct in answers
                           if ans == correct)
                total = len(algo['quiz'])
                st.success(f"Score: {score}/{total}")
                if score == total:
                    st.balloons()
                    st.markdown("🏆 **Perfect! You're a true Ninja!**")
                elif score >= total//2:
                    st.markdown("💪 **Good job! Keep practicing!**")
                else:
                    st.markdown("📚 **Keep studying — ninjas never give up!**")

                # Show correct answers
                st.subheader("Answers:")
                for i, (q, (ans, correct)) in enumerate(
                        zip(algo['quiz'], answers)):
                    if ans == correct:
                        st.success(f"Q{i+1}: ✅ {correct}")
                    else:
                        st.error(f"Q{i+1}: ❌ Your answer: {ans} | "
                                 f"Correct: {correct}")

# ================================
# ALGORITHM RACE PAGE
# ================================
elif page == "⚡ Algorithm Race":
    st.title("⚡ Algorithm Race")
    st.write("Compare sorting algorithm performance on same data!")

    col1, col2 = st.columns(2)
    with col1:
        size = st.slider("Array Size", 100, 1000, 300)
    with col2:
        data_type = st.selectbox("Data Type",
            ["Random", "Nearly Sorted", "Reverse Sorted"])

    if st.button("🏁 Start Race!", type="primary"):
        if data_type == "Random":
            arr = [random.randint(1, 10000) for _ in range(size)]
        elif data_type == "Nearly Sorted":
            arr = list(range(size))
            for _ in range(size//10):
                i, j = random.randint(0,size-1), random.randint(0,size-1)
                arr[i], arr[j] = arr[j], arr[i]
        else:
            arr = list(range(size, 0, -1))

        results = {}

        # Bubble Sort
        a = arr.copy()
        start = time.time()
        n = len(a)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
                    swapped = True
            if not swapped: break
        results['Bubble Sort'] = (time.time()-start)*1000

        # Insertion Sort
        a = arr.copy()
        start = time.time()
        for i in range(1, len(a)):
            key = a[i]; j = i-1
            while j >= 0 and a[j] > key:
                a[j+1] = a[j]; j -= 1
            a[j+1] = key
        results['Insertion Sort'] = (time.time()-start)*1000

        # Merge Sort iterative
        def merge_sort_iter(arr):
            arr = arr.copy(); n = len(arr); width = 1
            while width < n:
                for i in range(0, n, 2*width):
                    left = arr[i:i+width]
                    right = arr[i+width:i+2*width]
                    merged = []; li = ri = 0
                    while li < len(left) and ri < len(right):
                        if left[li] <= right[ri]:
                            merged.append(left[li]); li += 1
                        else:
                            merged.append(right[ri]); ri += 1
                    merged += left[li:] + right[ri:]
                    arr[i:i+len(merged)] = merged
                width *= 2
            return arr

        start = time.time()
        merge_sort_iter(arr)
        results['Merge Sort'] = (time.time()-start)*1000

        # Quick Sort iterative
        def quick_sort_iter(arr):
            arr = arr.copy(); stack = [(0, len(arr)-1)]
            while stack:
                low, high = stack.pop()
                if low < high:
                    pivot = arr[high]; i = low-1
                    for j in range(low, high):
                        if arr[j] <= pivot:
                            i += 1
                            arr[i], arr[j] = arr[j], arr[i]
                    arr[i+1], arr[high] = arr[high], arr[i+1]
                    pi = i+1
                    stack.append((low, pi-1))
                    stack.append((pi+1, high))
            return arr

        start = time.time()
        quick_sort_iter(arr)
        results['Quick Sort'] = (time.time()-start)*1000

        # Python Built-in
        start = time.time()
        sorted(arr)
        results['Python Built-in'] = (time.time()-start)*1000

        # Display results
        winner = min(results, key=results.get)
        loser = max(results, key=results.get)

        fig, ax = plt.subplots(figsize=(10, 5))
        colors = ['#1D9E75' if k == winner else
                  '#E24B4A' if k == loser else
                  '#378ADD'
                  for k in results.keys()]
        bars = ax.bar(results.keys(), results.values(), color=colors)
        ax.set_title(f'Algorithm Race — {size} elements ({data_type})')
        ax.set_ylabel('Time (milliseconds)')
        for bar, val in zip(bars, results.values()):
            ax.text(bar.get_x() + bar.get_width()/2,
                    bar.get_height() + 0.1,
                    f'{val:.2f}ms', ha='center', fontweight='bold')
        plt.tight_layout()
        st.pyplot(fig)

        st.success(f"🏆 Winner: **{winner}** — {results[winner]:.2f}ms")
        st.error(f"🐢 Slowest: **{loser}** — {results[loser]:.2f}ms")

        sorted_results = sorted(results.items(), key=lambda x: x[1])
        medals = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
        for i, (algo, t) in enumerate(sorted_results):
            st.write(f"{medals[i]} **{algo}**: {t:.2f}ms")

# ================================
# COMPLEXITY TABLE PAGE
# ================================
elif page == "📊 Complexity Table":
    st.title("📊 Algorithm Complexity Table")

    df = pd.DataFrame(complexity_data)
    st.dataframe(df, hide_index=True, use_container_width=True)

    st.divider()
    st.subheader("📈 Big O Complexity Visualized")

    n = np.linspace(1, 20, 100)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(n, np.ones_like(n), label='O(1) Constant', linewidth=2)
    ax.plot(n, np.log2(n), label='O(log n) Logarithmic', linewidth=2)
    ax.plot(n, n, label='O(n) Linear', linewidth=2)
    ax.plot(n, n*np.log2(n), label='O(n log n) Linearithmic', linewidth=2)
    ax.plot(n, n**2, label='O(n²) Quadratic', linewidth=2)
    ax.set_ylim(0, 200)
    ax.set_xlabel('Input Size (n)')
    ax.set_ylabel('Operations')
    ax.set_title('Big O Complexity Comparison')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)

    st.divider()
    st.subheader("🎯 Complexity Calculator")
    n_val = st.slider("Enter n (input size)", 1, 1000, 100)

    calc_data = {
        "Complexity": ["O(1)", "O(log n)", "O(n)",
                        "O(n log n)", "O(n²)"],
        "Operations": [
            1,
            round(np.log2(n_val), 2),
            n_val,
            round(n_val * np.log2(n_val), 2),
            n_val ** 2
        ]
    }
    st.table(pd.DataFrame(calc_data))

# ================================
# QUIZ MODE PAGE
# ================================
elif page == "🧩 Quiz Mode":
    st.title("🧩 Quiz Mode")
    st.write("Test your algorithm knowledge!")

    # Collect all questions
    all_questions = []
    for cat in algorithms.values():
        for algo in cat.values():
            for q in algo['quiz']:
                q_copy = q.copy()
                q_copy['algo'] = algo['full_name']
                all_questions.append(q_copy)

    col1, col2 = st.columns(2)
    with col1:
        num_q = st.slider("Number of questions",
                          3, len(all_questions), 10)
    with col2:
        category_filter = st.selectbox("Category",
            ["All"] + list(algorithms.keys()))

    if category_filter != "All":
        filtered = [q for q in all_questions
                   if any(q['algo'] == a['full_name']
                         for a in algorithms[category_filter].values())]
    else:
        filtered = all_questions

    if st.button("🎯 Generate Quiz", type="primary"):
        selected = random.sample(filtered,
                                  min(num_q, len(filtered)))
        st.session_state.quiz_questions = selected
        st.session_state.quiz_started = True
        st.session_state.quiz_submitted = False
        st.rerun()

    if st.session_state.get('quiz_started'):
        answers = []
        for i, q in enumerate(st.session_state.quiz_questions):
            st.markdown(f"**Q{i+1} [{q['algo']}]:** {q['question']}")
            ans = st.radio("", q['options'],
                           key=f"qmode_{i}_{q['question'][:20]}",
                           index=None)
            answers.append((ans, q['answer']))
            st.divider()

        if st.button("Submit All ✅", type="primary"):
            score = sum(1 for ans, correct in answers
                       if ans == correct)
            total = len(st.session_state.quiz_questions)
            percentage = (score/total)*100

            st.success(f"Final Score: {score}/{total} "
                       f"({percentage:.0f}%)")

            if percentage == 100:
                st.balloons()
                st.markdown("🥷 **You are a true AlgoNinja!**")
            elif percentage >= 70:
                st.markdown("💪 **Great job! Almost a ninja!**")
            elif percentage >= 50:
                st.markdown("📚 **Keep practicing!**")
            else:
                st.markdown("🔄 **Review the algorithms and try again!**")

            st.subheader("Answer Review:")
            for i, (q, (ans, correct)) in enumerate(
                    zip(st.session_state.quiz_questions, answers)):
                if ans == correct:
                    st.success(f"Q{i+1} ✅ {correct}")
                else:
                    st.error(f"Q{i+1} ❌ Your: {ans} | "
                             f"Correct: {correct}")

# ================================
# INTERVIEW PREP PAGE
# ================================
elif page == "🎯 Interview Prep":
    st.title("🎯 Interview Prep Mode")
    st.write("Practice real interview questions — timed like actual interviews!")

    col1, col2, col3 = st.columns(3)
    with col1:
        difficulty = st.selectbox("Difficulty",
            ["All", "Easy", "Medium", "Hard"])
    with col2:
        show_timer = st.checkbox("⏱️ Show Timer", value=True)
    with col3:
        st.metric("Total Questions", len(interview_questions))

    # Filter questions
    if difficulty == "All":
        filtered_q = interview_questions
    else:
        filtered_q = [q for q in interview_questions
                      if q['difficulty'] == difficulty]

    # Stats
    easy = len([q for q in interview_questions if q['difficulty']=='Easy'])
    medium = len([q for q in interview_questions if q['difficulty']=='Medium'])
    hard = len([q for q in interview_questions if q['difficulty']=='Hard'])

    c1, c2, c3 = st.columns(3)
    with c1: st.metric("🟢 Easy", easy)
    with c2: st.metric("🟡 Medium", medium)
    with c3: st.metric("🔴 Hard", hard)

    st.divider()

    # ===== PRACTICE MODE =====
    tab1, tab2 = st.tabs(["🎯 Practice Mode", "📚 Browse All Questions"])

    with tab1:
        if st.button("🎯 Get Random Question", type="primary"):
            q = random.choice(filtered_q)
            st.session_state.interview_q = q
            st.session_state.show_answer = False
            st.session_state.start_time = time.time()
            st.session_state.q_count = st.session_state.get('q_count', 0) + 1

        if st.session_state.get('interview_q'):
            q = st.session_state.interview_q
            diff_color = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

            # Question card
            st.markdown(f"### {diff_color[q['difficulty']]} Question #{st.session_state.get('q_count', 1)}")

        

            st.info(f"**{q['question']}**")

            

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("💡 Show Answer", type="primary"):
                    st.session_state.show_answer = True
            with col2:
                if st.button("➡️ Next Question"):
                    q = random.choice(filtered_q)
                    st.session_state.interview_q = q
                    st.session_state.show_answer = False
                    st.session_state.start_time = time.time()
                    st.session_state.q_count = st.session_state.get('q_count', 0) + 1
                    st.rerun()
            with col3:
                if st.button("🔀 Surprise Me!"):
                    q = random.choice(interview_questions)
                    st.session_state.interview_q = q
                    st.session_state.show_answer = False
                    st.session_state.start_time = time.time()
                    st.session_state.q_count = st.session_state.get('q_count', 0) + 1
                    st.rerun()

            if st.session_state.get('show_answer'):
                st.success(f"✅ **Answer:**\n\n{q['answer']}")

                # Self assessment
                st.markdown("**How did you do?**")
                c1, c2, c3 = st.columns(3)
                with c1:
                    if st.button("😊 Got it!"):
                        st.balloons()
                with c2:
                    if st.button("😐 Almost"):
                        st.info("Review this topic and try again!")
                with c3:
                    if st.button("😞 Missed it"):
                        st.warning("Don't worry — practice makes perfect! 💪")

        else:
            st.info("👆 Click 'Get Random Question' to start practicing!")

            # Ticking timer using auto-refresh
        if show_timer and 'start_time' in st.session_state:
            start_ts = int(st.session_state.start_time * 1000)
            time_limit = 45
            st.components.v1.html(f"""
            <div id="timer-container" style="
                background: #1a1a2e;
                border-radius: 8px;
                padding: 6px 16px;
                display: inline-block;
                margin: 10px 0;
                border: 2px solid #00ff88;">
                <span id="timer-label" style="
                    color: #00ff88;
                    font-size: 18px;
                    font-weight: bold;
                    font-family: monospace;">
                    ⏱️ 00:00
                </span>
            </div>

            <!-- Popup rendered INSIDE iframe so it's fully visible -->
            <div id="time-up-popup" style="
                display: none;
                position: fixed;
                top: 0; left: 0;
                width: 100vw;
                height: 100vh;
                background: rgba(0,0,0,0.92);
                z-index: 99999;
                justify-content: center;
                align-items: center;
                flex-direction: column;">
                <div style="
                    background: #1a1a2e;
                    border: 3px solid #ff4444;
                    border-radius: 20px;
                    padding: 40px 50px;
                    text-align: center;
                    width: 380px;
                    box-shadow: 0 0 40px rgba(255,68,68,0.5);">
                    <div style="font-size: 60px; margin-bottom: 10px;">⏰</div>
                    <h2 style="color: #ff4444; margin: 0 0 10px;">Time's Up!</h2>
                    <p style="color: #aaa; margin: 0 0 20px; font-size: 15px;">
                        60 seconds elapsed!<br>Did you know the answer?
                    </p>
                    <div style="display: flex; gap: 12px; justify-content: center;">
                        <button onclick="closePopup('yes')" style="
                            background: #00ff88;
                            color: #000;
                            border: none;
                            padding: 12px 24px;
                            border-radius: 25px;
                            font-size: 15px;
                            font-weight: bold;
                            cursor: pointer;">
                            ✅ Got it!
                        </button>
                        <button onclick="closePopup('no')" style="
                            background: #ff4444;
                            color: #fff;
                            border: none;
                            padding: 12px 24px;
                            border-radius: 25px;
                            font-size: 15px;
                            font-weight: bold;
                            cursor: pointer;">
                            ❌ Missed it
                        </button>
                    </div>
                </div>
            </div>

            <script>
                const startTime = {start_ts};
                const timeLimit = {time_limit};
                let popupShown = false;
                let timerStopped = false;
                let intervalId = null;

                function closePopup(result) {{
                    document.getElementById('time-up-popup').style.display = 'none';
                    const label = document.getElementById('timer-label');
                    if (result === 'yes') {{
                        label.textContent = '✅ Time up — you knew it!';
                        label.style.color = '#00ff88';
                    }} else {{
                        label.textContent = '📚 Time up — keep practicing!';
                        label.style.color = '#ff4444';
                    }}
                }}

                function updateTimer() {{
                    if (timerStopped) return;

                    const now = Date.now();
                    const elapsed = Math.floor((now - startTime) / 1000);

                    // Stop at time limit
                    if (elapsed >= timeLimit) {{
                        timerStopped = true;
                        clearInterval(intervalId);

                        // Show final time
                        const mins = Math.floor(timeLimit / 60);
                        const secs = timeLimit % 60;
                        const label = document.getElementById('timer-label');
                        label.textContent = '⏱️ ' +
                            String(mins).padStart(2,'0') + ':' +
                            String(secs).padStart(2,'0');
                        label.style.color = '#ff4444';
                        document.getElementById('timer-container').style.borderColor = '#ff4444';

                        // Show popup
                        if (!popupShown) {{
                            popupShown = true;
                            document.getElementById('time-up-popup').style.display = 'flex';
                        }}
                        return;
                    }}

                    const mins = Math.floor(elapsed / 60);
                    const secs = elapsed % 60;
                    const label = document.getElementById('timer-label');
                    label.textContent = '⏱️ ' +
                        String(mins).padStart(2,'0') + ':' +
                        String(secs).padStart(2,'0');

                    // Color changes
                    const container = document.getElementById('timer-container');
                    if (elapsed < 30) {{
                        label.style.color = '#00ff88';
                        container.style.borderColor = '#00ff88';
                    }} else if (elapsed < 50) {{
                        label.style.color = '#ffaa00';
                        container.style.borderColor = '#ffaa00';
                    }} else {{
                        label.style.color = '#ff4444';
                        container.style.borderColor = '#ff4444';
                    }}
                }}

                intervalId = setInterval(updateTimer, 1000);
                updateTimer();
            </script>
            """, height=250, scrolling=False)

    # ===== BROWSE ALL QUESTIONS =====
    with tab2:
        st.subheader(f"📚 All {len(filtered_q)} Questions — {difficulty}")

        search_q = st.text_input("🔍 Search questions...",
                                  placeholder="e.g. sorting, BFS, DP...")

        display_q = filtered_q
        if search_q:
            display_q = [q for q in filtered_q
                        if search_q.lower() in q['question'].lower() or
                           search_q.lower() in q['answer'].lower()]
            st.info(f"Found {len(display_q)} matching questions")

        diff_color = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}

        for i, q in enumerate(display_q):
            with st.expander(
                f"{diff_color[q['difficulty']]} Q{i+1}: {q['question'][:60]}..."):
                st.markdown(f"**Question:** {q['question']}")
                st.markdown(f"**Difficulty:** {diff_color[q['difficulty']]} {q['difficulty']}")
                st.divider()
                st.success(f"**Answer:** {q['answer']}")


# ================================
# SEARCH PAGE
# ================================
elif page == "🔍 Search Algorithm":
    st.title("🔍 Search Algorithm")
    search = st.text_input("Search any algorithm...",
        placeholder="e.g. BFS, sorting, dynamic, graph...")

    if search:
        found = []
        for cat, algos in algorithms.items():
            for name, data in algos.items():
                if (search.lower() in name.lower() or
                    search.lower() in data['full_name'].lower() or
                    search.lower() in data['description'].lower() or
                    search.lower() in cat.lower()):
                    found.append((cat, name, data))

        if found:
            st.success(f"Found {len(found)} result(s) "
                       f"for '{search}'")
            for cat, name, data in found:
                diff_color = {"Easy":"🟢","Medium":"🟡","Hard":"🔴"}
                with st.expander(
                    f"{diff_color.get(data['difficulty'],'⚪')} "
                    f"**{data['full_name']}** — {cat}"):
                    st.markdown(data['description'])
                    st.divider()
                    st.subheader("Python Code:")
                    st.code(data['code']['Python'], language='python')
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Time", data['time_complexity'])
                    with col2:
                        st.metric("Space", data['space_complexity'])
                    with col3:
                        st.metric("Difficulty", data['difficulty'])
        else:
            st.error(f"No results for '{search}'. "
                     f"Try: BFS, sorting, dynamic, graph, agent...")
            st.info("Available algorithms: " +
                    ", ".join(name for cat in algorithms.values()
                             for name in cat.keys()))
