document.addEventListener('DOMContentLoaded', function() {
  const chartData = JSON.parse(document.getElementById('chart-data').textContent);

  const ctx = document.getElementById('workoutChart').getContext('2d');
  const workoutChart = new Chart(ctx, {
      type: 'bar',
      data: {
          labels: chartData.map(data => data.exercise_name),
          datasets: [{
              label: 'Total Sets',
              data: chartData.map(data => data.total_sets),
              backgroundColor: 'rgba(255, 99, 132, 0.5)',
              borderColor: 'rgba(255, 99, 132, 1)',
              borderWidth: 1
          }, {
              label: 'Total Reps',
              data: chartData.map(data => data.total_reps),
              backgroundColor: 'rgba(54, 162, 235, 0.5)',
              borderColor: 'rgba(54, 162, 235, 1)',
              borderWidth: 1
          }, {
              label: 'Total Weight',
              data: chartData.map(data => data.total_weight),
              backgroundColor: 'rgba(255, 206, 86, 0.5)',
              borderColor: 'rgba(255, 206, 86, 1)',
              borderWidth: 1
          }]
      },
      options: {
          scales: {
              y: {
                  beginAtZero: true
              }
          }
      }
  });
});
