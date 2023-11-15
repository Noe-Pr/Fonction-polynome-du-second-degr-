document.addEventListener("DOMContentLoaded", function () {
    const resolveButton = document.getElementById("resolve-btn");
    const equationResult = document.getElementById("equation-result");
    const plotCanvas = document.getElementById("plot-canvas");
    const ctx = plotCanvas.getContext("2d");

    resolveButton.addEventListener("click", resolveEquation);

    // Ajoutez un gestionnaire d'événements pour chaque champ d'entrée
    const inputFields = document.querySelectorAll(".input-field");
    inputFields.forEach((input) => {
        input.addEventListener("input", validateInput);
        input.addEventListener("keydown", handleEnterKey);
    });

    function validateInput(event) {
        const input = event.target;
        const inputValue = input.value;

        // Remplacez tous les caractères non autorisés par une chaîne vide
        const sanitizedValue = inputValue.replace(/[^0-9.\-]/g, "");

        // Mettez la valeur filtrée dans le champ d'entrée
        input.value = sanitizedValue;
    }

    function resolveEquation() {
        // Vérifiez si tous les champs sont remplis
        const a = parseFloat(document.getElementById("a").value);
        const b = parseFloat(document.getElementById("b").value);
        const c = parseFloat(document.getElementById("c").value);

        if (isNaN(a) || isNaN(b) || isNaN(c)) {
            equationResult.innerHTML = "Veuillez remplir tous les champs.";
            return;
        }

        const delta = b ** 2 - 4 * a * c;
        equationResult.innerHTML = `Δ = ${delta}`;
        if (delta < 0) {
            equationResult.innerHTML += `<br>L'équation ${a}x² + ${b}x + ${c} = 0 n'a pas de solution.`;
        } else if (delta === 0) {
            const x0 = -b / (2 * a);
            equationResult.innerHTML += `<br>L'équation ${a}x² + ${b}x + ${c} = 0 a une solution : x0 = ${x0.toFixed(2)}`;
        } else {
            const x1 = (-b - Math.sqrt(delta)) / (2 * a);
            const x2 = (-b + Math.sqrt(delta)) / (2 * a);
            equationResult.innerHTML += `<br>L'équation ${a}x² + ${b}x + ${c} = 0 a deux solutions distinctes : x1 = ${x1.toFixed(2)} et x2 = ${x2.toFixed(2)}`;
        }
        plotGraph(a, b, c);
    }

    function handleEnterKey(event) {
        if (event.key === "Enter") {
            resolveEquation();
            event.preventDefault(); // Empêche le comportement par défaut de la touche Entrée (soumission du formulaire)
        }
    }

    function plotGraph(a, b, c) {
        ctx.clearRect(0, 0, plotCanvas.width, plotCanvas.height);

        // Dessiner le cadrillage en arrière-plan
        ctx.strokeStyle = "lightgray";
        ctx.lineWidth = 1;
        for (let x = -10; x <= 10; x++) {
            ctx.beginPath();
            ctx.moveTo(x * 40 + plotCanvas.width / 2, 0);
            ctx.lineTo(x * 40 + plotCanvas.width / 2, plotCanvas.height);
            ctx.stroke();
            ctx.beginPath();
            ctx.moveTo(0, -x * 40 + plotCanvas.height / 2);
            ctx.lineTo(plotCanvas.width, -x * 40 + plotCanvas.height / 2);
            ctx.stroke();
        }

        // Dessiner la courbe en bleu
        ctx.strokeStyle = "blue";
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = -10; x <= 10; x += 0.1) {
            const y = a * x * x + b * x + c;
            const plotX = x * 40 + plotCanvas.width / 2;
            const plotY = -y * 40 + plotCanvas.height / 2;
            if (x === -10) {
                ctx.moveTo(plotX, plotY);
            } else {
                ctx.lineTo(plotX, plotY);
            }
        }
        ctx.stroke();

        // Dessiner les axes en noir
        ctx.strokeStyle = "black";
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(plotCanvas.width / 2, 0);
        ctx.lineTo(plotCanvas.width / 2, plotCanvas.height);
        ctx.moveTo(0, plotCanvas.height / 2);
        ctx.lineTo(plotCanvas.width, plotCanvas.height / 2);
        ctx.stroke();
    }
});
