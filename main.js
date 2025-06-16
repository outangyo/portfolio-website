document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById('toggle-resume-btn');
    const resumeContent = document.getElementById('resume-content');

    if (toggleBtn && resumeContent) {
        toggleBtn.addEventListener('click', function () {
            const isVisible = resumeContent.style.display === 'block';

            resumeContent.style.display = isVisible ? 'none' : 'block';
            toggleBtn.textContent = isVisible ? 'Preview My Resume' : 'Hide Preview';
        });
    }
});