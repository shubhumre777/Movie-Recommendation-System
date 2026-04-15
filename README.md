<!-- ================= HEADER ================= -->

<h1 align="center">🎬 Movie Recommendation System</h1>

<p align="center">
  <b>Smart movie recommendations powered by Machine Learning & deployed with Streamlit</b>
</p>

<p align="center">
  <a href="https://movie-recommendation-s-umre.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🚀 Live%20Demo-Click%20Here-success?style=for-the-badge" />
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Deployed-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Machine%20Learning-TF--IDF-green?style=for-the-badge" />
</p>

---

<!-- ================= LIVE DEMO ================= -->

<h2>🌐 Live Application</h2>

<p>
Experience the app here:<br><br>
👉 <a href="https://movie-recommendation-s-umre.streamlit.app/" target="_blank">
<b>Movie Recommendation System (Live)</b>
</a>
</p>

---

<!-- ================= ABOUT ================= -->

<h2>📌 About the Project</h2>

<p>
This is a <b>content-based movie recommendation system</b> that suggests similar movies based on user selection.  
It uses <b>TF-IDF vectorization</b> and <b>cosine similarity</b> to compute relationships between movies.
</p>

<p>
The app also integrates with the <b>TMDB API</b> to fetch high-quality movie posters dynamically, providing a visually rich experience.
</p>

---

<!-- ================= FEATURES ================= -->

<h2>🚀 Features</h2>

<ul>
  <li>🎯 Intelligent movie recommendations</li>
  <li>⚡ Fast similarity computation using TF-IDF</li>
  <li>🖼️ Real-time movie posters from TMDB API</li>
  <li>🎲 Random movie browsing interface</li>
  <li>🎨 Clean dark-themed UI</li>
  <li>📱 Fully interactive Streamlit application</li>
</ul>

---

<!-- ================= HOW IT WORKS ================= -->

<h2>🧠 How It Works</h2>

<p>
The system converts movie data into numerical vectors using <b>TF-IDF</b>, then calculates similarity scores using 
<b>cosine similarity</b>. The top similar movies are returned as recommendations.
</p>

<pre>
User selects a movie
        ↓
TF-IDF vectorization
        ↓
Cosine similarity calculation
        ↓
Top 5 similar movies displayed
</pre>

---

<!-- ================= TECH STACK ================= -->

<h2>🏗️ Tech Stack</h2>

<table>
  <tr>
    <td><b>Frontend</b></td>
    <td>Streamlit</td>
  </tr>
  <tr>
    <td><b>Backend</b></td>
    <td>Python</td>
  </tr>
  <tr>
    <td><b>Machine Learning</b></td>
    <td>Scikit-learn (TF-IDF, Cosine Similarity)</td>
  </tr>
  <tr>
    <td><b>API</b></td>
    <td>TMDB API</td>
  </tr>
  <tr>
    <td><b>Data Processing</b></td>
    <td>Pandas, Pickle</td>
  </tr>
</table>

---

<!-- ================= PROJECT STRUCTURE ================= -->

<h2>📂 Project Structure</h2>

<pre>
Movie-Recommendation-System/
│
├── app.py
├── df.pkl
├── indices.pkl
├── tfidf_matrix.pkl
├── data/
│   └── movies_metadata.csv
├── requirements.txt
└── README.md
</pre>

---

<!-- ================= INSTALLATION ================= -->

<h2>⚙️ Installation & Setup</h2>

<h3>1. Clone Repository</h3>

<pre>
git clone https://github.com/shubhumre777/Movie-Recommendation-System.git
cd Movie-Recommendation-System
</pre>

<h3>2. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>3. Run the App</h3>

<pre>
streamlit run app.py
</pre>

---

<!-- ================= API ================= -->

<h2>🔑 API Configuration</h2>

<p>
This project uses <b>TMDB API</b> to fetch movie posters.
</p>

<pre>
API_KEY = "your_api_key_here"
</pre>

---

<!-- ================= CONTRIBUTING ================= -->

<h2>🤝 Contributing</h2>

<p>
Feel free to fork this repository and contribute by submitting a pull request.
</p>

---

<!-- ================= LICENSE ================= -->

<h2>📜 License</h2>

<p>
This project is licensed under the <b>MIT License</b>.
</p>

---

<!-- ================= AUTHOR ================= -->

<h2 align="center">👨‍💻 Author</h2>

<p align="center">
  <b>Shubh Umre</b><br>
  <a href="https://github.com/shubhumre777">GitHub Profile</a>
</p>

<p align="center">⭐ Star this repo if you found it intresting</p>
