function checkPassword() {
    const password = document.getElementById("password").value;

    fetch("/check", {
        method: "POST",
        body: new URLSearchParams({ "password": password }),
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
    })
    .then(res => res.json())
    .then(data => {
        let level = data.level;
        let score = data.score;
        let bar = document.getElementById("bar");
        let result = document.getElementById("result");
        let log = document.getElementById("logOutput");

        if (level === "Strong") {
            bar.style.width = "100%";
            bar.style.background = "lime";
        } else if (level === "Medium") {
            bar.style.width = "60%";
            bar.style.background = "orange";
        } else {
            bar.style.width = "30%";
            bar.style.background = "red";
        }

        result.textContent = "Password Strength: " + level;

        const timestamp = new Date().toLocaleTimeString();
        log.textContent += `[${timestamp}] Checked Password ➜ ${level}\n`;
    });
}
