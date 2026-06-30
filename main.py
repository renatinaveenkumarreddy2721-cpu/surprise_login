from flask import Flask, render_template_string, request

app = Flask(__name__)

# Login page
login_page = """
<!doctype html>
<html>
<head><title>Surprise Login</title></head>
<body style="text-align:center; font-family:Arial;">
    <h2>Welcome! Please Login</h2>
    <form method="POST" action="/login">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>
        <label>Date of Birth (DD-MM-YYYY):</label><br>
        <input type="text" name="dob" required><br><br>
        <button type="submit">Login</button>
    </form>
</body>
</html>
"""

# Surprise page with hearts, music, and background image
surprise_page = """
<!doctype html>
<html>
<head>
    <title>Surprise</title>
    <style>
        body {
            text-align:center;
            font-family:Arial;
            background-image: url('https://images.unsplash.com/photo-1509042239860-f550ce710b93'); /* Roses background */
            background-size: cover;
            background-position: center;
            color: white;
            overflow:hidden;
        }
        .heart {
            position: absolute;
            color: red;
            font-size: 24px;
            animation: float 5s infinite;
        }
        @keyframes float {
            0% { transform: translateY(0); opacity: 1; }
            100% { transform: translateY(-600px); opacity: 0; }
        }
        h1, h2, p {
            background-color: rgba(0,0,0,0.5);
            display: inline-block;
            padding: 10px;
            border-radius: 10px;
        }
    </style>
</head>
<body>
    <h1>💖 Hello {{name}} 💖</h1>
    <h2>I Love You Forever 💕</h2>
    <p>Your DOB: {{dob}}</p>

    <!-- Background music -->
    <audio autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
    </audio>

    <!-- Floating hearts -->
    <script>
        function createHeart() {
            const heart = document.createElement("div");
            heart.className = "heart";
            heart.innerHTML = "❤️";
            heart.style.left = Math.random() * window.innerWidth + "px";
            heart.style.top = window.innerHeight + "px";
            document.body.appendChild(heart);
            setTimeout(() => heart.remove(), 5000);
        }
        setInterval(createHeart, 500);
    </script>
</body>
</html>
"""

# Error page if wrong login
error_page = """
<!doctype html>
<html>
<head><title>Access Denied</title></head>
<body style="text-align:center; font-family:Arial; background-color:#f8d7da;">
    <h2>❌ Access Denied ❌</h2>
    <p>Sorry, only Vyshnavi can see the surprise!</p>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(login_page)

@app.route('/login', methods=['POST'])
def login():
    name = request.form.get("name")
    dob = request.form.get("dob")
    if name.lower() == "vyshnavi" and dob == "21-12-2006":
        return render_template_string(surprise_page, name=name, dob=dob)
    else:
        return render_template_string(error_page)

if __name__ == '__main__':
    app.run(debug=True)
