var labels = [
  "25 Sep",
  "29 Sep",
  "2 Oct",
  "7 Oct",
  "10 Oct",
  "15 Oct",
  "22 Oct",
];

var config = {
  type: "line",
  data: {
    labels: labels,
    datasets: [
      {
        label: "Deadlift PR",
        data: [100, 100, 110, 110, 110, 120, 120],
        fill: false,
        borderColor: "#f2c02c",
        tension: 0.1,
      },
    ],
    options: {
      legend: {
        display: true,
        position: "bottom",
        labels: {
          // color: "#000000",
        },
      },
    },
  },
};

var ctxOne = document.getElementById("line-chart").getContext("2d");
new Chart(ctxOne, config);

$("#recipeCarousel").carousel({
  interval: 10000,
});

$(".carousel .carousel-item").each(function () {
  var minPerSlide = 3;
  var next = $(this).next();
  if (!next.length) {
    next = $(this).siblings(":first");
  }
  next.children(":first-child").clone().appendTo($(this));

  for (var i = 0; i < minPerSlide; i++) {
    next = next.next();
    if (!next.length) {
      next = $(this).siblings(":first");
    }

    next.children(":first-child").clone().appendTo($(this));
  }
});
