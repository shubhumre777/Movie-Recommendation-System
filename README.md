<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MovieRec | ML Showcase</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary: #e50914;
            --bg: #0a0a0a;
            --card-bg: rgba(255, 255, 255, 0.05);
            --text: #ffffff;
            --accent: #ff4d4d;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }

        body {
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.6;
            overflow-x: hidden;
        }

        /* Hero Section */
        .hero {
            height: 60vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background: linear-gradient(rgba(0,0,0,0.7), rgba(10,10,10,1)), 
                        url('https://images.unsplash.com/photo-1485846234645-a62644f84728?auto=format&fit=crop&q=80&w=2000');
            background-size: cover;
            background-position: center;
            padding: 20px;
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 10px;
            letter-spacing: -1px;
            animation: fadeInDown 1s ease;
        }

        .badge {
            background: var(--primary);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9rem;
            font-weight: bold;
            text-transform: uppercase;
        }

        /* Main Content */
        .container {
            max-width: 1000px;
            margin: -50px auto 50px;
            padding: 0 20px;
        }

        .glass-card {
            background: var(--card-bg);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 20px;
            padding: 40px;
            margin-bottom: 30px;
            transition: transform 0.3s ease;
        }

        .glass-card:hover {
            transform: translateY(-5px);
        }

        h2 {
            color: var(--primary);
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* Features Grid */
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .feature-item {
            background: rgba(255,255,255,0.03);
            padding: 20px;
            border-radius: 15px;
            border-left: 4px solid var(--primary);
        }

        /* Tech Stack */
        .tech-pill {
            display: inline-block;
            background: rgba(255,255,255,0.1);
            padding: 8px 18px;
            border-radius: 50px;
            margin: 5px;
            font-size: 0.9rem;
            transition: 0.3s;
        }

        .tech-pill:hover {
            background: var(--primary);
        }

        /* Code Block Styling */
        pre {
            background: #000;
            padding: 20px;
            border-radius: 10px;
            overflow-x: auto;
            border: 1px solid #333;
            color: #00ff00;
            font-family: 'Courier New', monospace;
        }

        /* Math Section */
        .math-box {
            text-align: center;
            padding: 20px;
            background: rgba(229, 9, 20, 0.05);
            border-radius: 15px;
            font-style: italic;
        }

        /* Animations */
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s ease-out;
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        footer {
            text-align: center;
            padding: 40px;
            border-top: 1px solid #333;
        }

        .btn-github {
            text-decoration: none;
            color: white;
            background: #333;
            padding: 12px 25px;
            border-radius: 10px;
            display: inline-flex;
            align-items: center;
            gap: 10px;
            margin-top: 20px;
            transition: 0.3s;
        }

        .btn-github:hover {
            background: #555;
        }
    </style>
</head>
<body>

    <section class="hero">
        <span class="badge">Machine Learning Project</span>
        <h1>Movie Recommendation System</h1>
        <p>Intelligent discovery powered by TF-IDF & Cosine Similarity</p>
    </section>

    <div class="container">
        <div class="glass-card reveal">
            <h2><i class="fas fa-rocket"></i> Project Overview</h2>
            <p>A sleek, intelligent recommendation engine built with Python and Streamlit. This application suggests movies similar to your selection by analyzing metadata and dynamically fetching high-quality posters via the TMDB API.</p>
        </div>

        <div class="glass-card reveal">
            <h2><i class="fas fa-star"></i> Core Features</h2>
            <div class="grid">
                <div class="feature-item">
                    <h4>Content-Based Engine</h4>
                    <p>Analyzes genres, keywords, and overviews to find the perfect match.</p>
                </div>
                <div class="feature-item">
                    <h4>Live TMDB Integration</h4>
                    <p>Fetches real-time movie posters and metadata dynamically.</p>
                </div>
                <div class="feature-item">
                    <h4>Fast Computation</h4>
                    <p>Optimized similarity matrix for near-instant results.</p>
                </div>
                <div class="feature-item">
                    <h4>Modern UI</h4>
                    <p>Custom dark-themed interface designed for movie enthusiasts.</p>
                </div>
            </div>
        </div>

        <div class="glass-card reveal">
            <h2><i class="fas fa-brain"></i> The Intelligence</h2>
            <p>The system transforms movie text data into numerical vectors using <strong>TF-IDF</strong> (Term Frequency-Inverse Document Frequency). Similarity is then calculated using the Cosine Similarity formula:</p>
            <div class="math-box">
                Similarity = cos(θ) = (A · B) / (||A|| ||B||)
            </div>
            <p style="margin-top:15px;">By measuring the cosine of the angle between two vectors, the system determines how closely related two movies are regardless of their metadata length.</p>
        </div>

        <div class="glass-card reveal">
            <h2><i class="fas fa-layer-group"></i> Tech Stack</h2>
            <div class="tech-pill">Python</div>
            <div class="tech-pill">Streamlit</div>
            <div class="tech-pill">Scikit-Learn</div>
            <div class="tech-pill">Pandas</div>
            <div class="tech-pill">TMDB API</div>
            <div class="tech-pill">Pickle</div>
        </div>

        <div class="glass-card reveal">
            <h2><i class="fas fa-terminal"></i> Installation</h2>
            <pre>
# Clone repo
git clone https://github.com/shubhumre777/Movie-Recommendation-System.git

# Install requirements
pip install -r requirements.txt

# Launch Application
streamlit run app.py
            </pre>
        </div>
    </div>

    <footer>
        <p>Developed by <strong>Shubhum Re</strong></p>
        <a href="https://github.com/shubhumre777/Movie-Recommendation-System" class="btn-github">
            <i class="fab fa-github"></i> View on GitHub
        </a>
    </footer>

    <script>
        // Scroll Reveal Animation
        function reveal() {
            var reveals = document.querySelectorAll(".reveal");
            for (var i = 0; i < reveals.length; i++) {
                var windowHeight = window.innerHeight;
                var elementTop = reveals[i].getBoundingClientRect().top;
                var elementVisible = 150;
                if (elementTop < windowHeight - elementVisible) {
                    reveals[i].classList.add("active");
                }
            }
        }

        window.addEventListener("scroll", reveal);
        
        // Trigger once on load
        reveal();
    </script>
</body>
</html>
