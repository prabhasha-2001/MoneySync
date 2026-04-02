// Auto-dismiss bootstrap alerts after 5 seconds
setTimeout(function() {
    let alerts = document.querySelectorAll('.alert');
    alerts.forEach(function(alert) {
        let bsAlert = new bootstrap.Alert(alert);
        bsAlert.close();
    });
}, 5000);