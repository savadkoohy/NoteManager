// فایل script.js
document.addEventListener("DOMContentLoaded", function () {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
      setTimeout(() => {
        alert.classList.add('fade');
        alert.classList.remove('show');
      }, 4000); // حذف پیام بعد از ۴ ثانیه
    });
  });
  