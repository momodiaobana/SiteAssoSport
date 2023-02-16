function generateBarChart(count_boxe_items, count_foot_items, count_basket_items) {
    const ctx = document.getElementById('myChart');

    const labels = ['boxe', 'foot', 'basket'];
    const barres = {
        labels: labels,
        datasets: [{
            label: 'quantité',
            data: [count_boxe_items, count_foot_items, count_basket_items],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(75, 192, 192, 0.2)'
            ],
            borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgba(75, 192, 192)'
            ],
            borderWidth: 1
        }]
    };

    //quantité d'article par catégorie
    new Chart(ctx, {
        type: 'bar',
        data: barres,
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        },
    });
}


function generatePieChart(valeur_stock_boxe, valeur_stock_foot, valeur_stock_basket) {
    const ctx2 = document.getElementById('myChart2');

    const pie = {
        labels: ['Boxe', 'Foot', 'Basket'],
        datasets: [{
            label: 'Valeur en € ',
            data: [valeur_stock_boxe, valeur_stock_foot, valeur_stock_basket],
            backgroundColor: [
                'rgb(255, 99, 132)',
                'rgb(54, 162, 235)',
                'rgb(255, 205, 86)'
            ],
            hoverOffset: 3
        }]
    };

    //valeur de chaque caté 
    new Chart(ctx2, {
        type: 'pie',
        data: pie,
    });
}
