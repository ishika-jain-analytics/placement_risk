const circle = document.getElementById("progressRing");
const radius = 75;
const circumference = 2 * Math.PI * radius;

circle.style.strokeDasharray = circumference;

const offset = circumference - (percent / 100) * circumference;

setTimeout(() => {
    circle.style.strokeDashoffset = offset;
}, 300);


// PIE CHART (dynamic)
let pieData;

if (risk === "LOW") pieData = [10, 20, 70];
else if (risk === "MEDIUM") pieData = [20, 50, 30];
else pieData = [60, 30, 10];

new Chart(document.getElementById("pieChart"), {
    type: "pie",
    data: {
        labels: ["High", "Medium", "Low"],
        datasets: [{
            data: pieData,
            backgroundColor: ["#ff4d4d", "#ff9800", "#00ff88"]
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { labels: { color: "white" } }
        }
    }
});


// BAR CHART
const ctx = document.getElementById("barChart").getContext("2d");
const gradient = ctx.createLinearGradient(0, 0, 0, 300);
gradient.addColorStop(0, "#00c6ff");
gradient.addColorStop(1, "#0072ff");

new Chart(ctx, {
    type: "bar",
    data: {
        labels: ["Tier 1", "Tier 2", "Tier 3"],
        datasets: [{
            label: "Avg Salary (LPA)",
            data: [12, 8, 5],
            backgroundColor: gradient,
            borderRadius: 10
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { labels: { color: "white" } }
        }
    }
});