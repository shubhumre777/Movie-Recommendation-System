<!-- ================= HEADER ================= -->

<h1 align="center">🎬 Movie Recommendation System</h1>

<p align="center">
  <b>A modern Machine Learning-powered movie recommendation app built with Streamlit</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Machine%20Learning-TF--IDF-green?style=for-the-badge" />
</p>

---

<!-- ================= ABOUT ================= -->

<h2>📌 About the Project</h2>

<p>
This project is a <b>content-based movie recommendation system</b> that suggests movies similar to a selected title using 
<b>TF-IDF vectorization</b> and <b>cosine similarity</b>.  
It also integrates with the <b>TMDB API</b> to dynamically fetch movie posters.
</p>

---

<!-- ================= FEATURES ================= -->

<h2>🚀 Features</h2>

<ul>
  <li>🎯 Content-based movie recommendations</li>
  <li>⚡ Fast similarity computation using TF-IDF</li>
  <li>🖼️ Dynamic movie posters via TMDB API</li>
  <li>🎲 Random movie browsing on homepage</li>
  <li>🎨 Dark-themed modern UI using Streamlit</li>
</ul>

---

<!-- ================= HOW IT WORKS ================= -->

<h2>🧠 How It Works</h2>

<p>
The system transforms movie data into numerical vectors using <b>TF-IDF</b>, then computes similarity between movies using 
<b>cosine similarity</b>. Based on this, it returns the most relevant recommendations.
</p>

<pre>
TF-IDF → Vectorization → Cosine Similarity → Top Recommendations
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
Contributions are welcome! Feel free to fork the repository and submit a pull request.
</p>

---

<!-- ================= LICENSE ================= -->

<h2>📜 License</h2>

<p>
This project is licensed under the <b>MIT License</b>.
</p>

---

<!-- ================= FOOTER ================= -->

<h2 align="center">👨‍💻 Author</h2>

<p align="center">
  <b>Shubhum Re</b><br>
  <a href="https://github.com/shubhumre777">GitHub Profile</a>
</p>

<p align="center">⭐ If you like this project, consider giving it a star!</p>
