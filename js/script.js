var weekdays = [
  "Понедельник",
  "Вторник",
  "Среда",
  "Четверг",
  "Пятница",
  "Суббота",
  "Воскресенье",
];

var config = {
  type: "line",
  data: {
    labels: weekdays,
    datasets: [
      {
        label: "Week of Training",
        data: [65, 59, 80, 81, 56, 55, 40],
        fill: false,
        label: "Label 1",
        borderColor: "#f2c02c",
        tension: 0.1,
      },
    ],
    options: {
      legend: { 
        display: true,
        position: "bottom",
        labels: {
          color: "#FFFFFF",
        },
      },
    },
  },
};

var ctxOne = document.getElementById("line-chart").getContext("2d");
new Chart(ctxOne, config);
