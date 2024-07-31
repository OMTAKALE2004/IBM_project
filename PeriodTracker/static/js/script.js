document.addEventListener('DOMContentLoaded', function() {
    const periodForm = document.getElementById('periodForm');
    const calendar = document.getElementById('calendar');
    const profileForm = document.getElementById('profileForm');

    periodForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const startDate = new Date(document.getElementById('start').value);
        const cycleLength = parseInt(document.getElementById('cycle').value);
        const bleedingDays = parseInt(document.getElementById('bleeding').value);
        displayCalendar(startDate, cycleLength, bleedingDays);
    });

    profileForm.addEventListener('submit', function(event) {
        event.preventDefault();
        profileForm.classList.add('hidden');
        alert('Profile saved successfully');
    });
});

function showProfileForm() {
    const profileForm = document.getElementById('profileForm');
    profileForm.classList.remove('hidden');
}

function displayCalendar(startDate, cycleLength, bleedingDays) {
    const calendar = document.getElementById('calendar');
    calendar.innerHTML = '';

    const months = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];

    for (let m = 0; m < 12; m++) {
        const monthDiv = document.createElement('div');
        monthDiv.classList.add('month');
        const monthTitle = document.createElement('h2');
        monthTitle.textContent = months[m];
        monthDiv.appendChild(monthTitle);
        
        const daysDiv = document.createElement('div');
        daysDiv.classList.add('days');

        const firstDay = new Date(startDate.getFullYear(), m, 1).getDay();
        const daysInMonth = new Date(startDate.getFullYear(), m + 1, 0).getDate();
        
        for (let i = 0; i < firstDay; i++) {
            const emptyDiv = document.createElement('div');
            emptyDiv.classList.add('day');
            daysDiv.appendChild(emptyDiv);
        }
        
        for (let d = 1; d <= daysInMonth; d++) {
            const dayDiv = document.createElement('div');
            dayDiv.classList.add('day');
            const currentDate = new Date(startDate.getFullYear(), m, d);

            if (isPeriodDay(startDate, currentDate, cycleLength, bleedingDays)) {
                dayDiv.classList.add('period');
            }
            if (isOvulationDay(startDate, currentDate, cycleLength)) {
                dayDiv.classList.add('ovulation');
            }
            
            dayDiv.textContent = d;
            daysDiv.appendChild(dayDiv);
        }
        
        monthDiv.appendChild(daysDiv);
        calendar.appendChild(monthDiv);
    }
}

function isPeriodDay(startDate, currentDate, cycleLength, bleedingDays) {
    const diff = (currentDate - startDate) / (1000 * 60 * 60 * 24);
    return diff % cycleLength >= 0 && diff % cycleLength < bleedingDays;
}

function isOvulationDay(startDate, currentDate, cycleLength) {
    const diff = (currentDate - startDate) / (1000 * 60 * 60 * 24);
    return diff % cycleLength >= (cycleLength / 2 - 1) && diff % cycleLength <= (cycleLength / 2 + 1);
}

function notifyPeriod() {
    alert('Time to log your period!');
}
