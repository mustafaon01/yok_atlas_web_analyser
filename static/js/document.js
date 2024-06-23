document.getElementById('filter-button').addEventListener('click', function () {
    let programCode = document.getElementById('program-code').value.toLowerCase();
    let universityName = document.getElementById('university-name').value.toLowerCase();
    let departmentName = document.getElementById('department-name').value.toLowerCase();

    let table = document.getElementById('data-table').getElementsByTagName('tbody')[0];
    let rows = table.getElementsByTagName('tr');

    for (let i = 0; i < rows.length; i++) {
        let programCodeCell = rows[i].getElementsByTagName('td')[1].textContent.toLowerCase();
        let universityNameCell = rows[i].getElementsByTagName('td')[3].textContent.toLowerCase();
        let departmentNameCell = rows[i].getElementsByTagName('td')[2].textContent.toLowerCase();

        if ((programCode === "" || programCodeCell.includes(programCode)) &&
            (universityName === "" || universityNameCell.includes(universityName)) &&
            (departmentName === "" || departmentNameCell.includes(departmentName))) {
            rows[i].style.display = "";
        } else {
            rows[i].style.display = "none";
        }
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const menuIcon = document.getElementById('menu-icon');
    menuIcon.addEventListener('click', function () {
    });
});
// Menü ikonuna tıklayınca listeyi göster/gizle
document.getElementById('menu-icon').addEventListener('click', function (event) {
    var tableList = document.getElementById('table-list');
    tableList.style.display = tableList.style.display === 'none' ? 'block' : 'none';
    event.stopPropagation(); // Bu tıklamanın belgedeki diğer olayları tetiklemesini engeller
});

// Liste öğesine tıklanınca ilgili tabloyu göster
document.querySelectorAll('#table-list li').forEach(function (item) {
    item.addEventListener('click', function (event) {
        var tableName = this.getAttribute('data-table');
        showTableSection(tableName);
        event.stopPropagation(); // Bu tıklamanın belgedeki diğer olayları tetiklemesini engeller
    });
});


function showTableSection(tableName) {
    // Tüm tablo bölümlerini gizle
    var sections = document.getElementsByClassName('content-section');
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }

    // Seçilen tablo bölümünü göster
    var sectionId = tableName + '-section';
    document.getElementById(sectionId).style.display = 'block';

    // Menü listesini gizle
    document.getElementById('table-list').style.display = 'none';
}

// Ekranın herhangi bir yerine tıklanınca listeyi gizle
document.addEventListener('click', function () {
    var tableList = document.getElementById('table-list');
    if (tableList.style.display === 'block') {
        tableList.style.display = 'none';
    }
});


function showTableSection(tableName) {
    // Tüm tablo bölümlerini gizle
    var sections = document.getElementsByClassName('content-section');
    for (var i = 0; i < sections.length; i++) {
        sections[i].style.display = 'none';
    }

    // Seçilen tablo bölümünü göster
    var sectionId = tableName + '-section';
    document.getElementById(sectionId).style.display = 'block';

    // Menü listesini gizle
    document.getElementById('table-list').style.display = 'none';
}


// Function to load CSV data into the table
function loadCSVData(filePath) {
    fetch(filePath)
        .then(response => response.text())
        .then(data => {
            let table = document.getElementById('data-table').getElementsByTagName('tbody')[0];
            let rows = data.split('\n');
            for (let i = 1; i < rows.length; i++) { // Skip the header row
                let cols = rows[i].split(',');
                if (cols.length > 1) { // Ensure it's a valid row
                    let row = table.insertRow();
                    for (let j = 0; j < cols.length; j++) {
                        let cell = row.insertCell();
                        cell.textContent = cols[j];
                    }
                }
            }
        })
        .catch(error => console.error('Error loading CSV data:', error));
}

// Load the CSV data when the page loads
window.onload = function () {
    loadCSVData('university_data.csv');

};
