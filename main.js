// Get the button and resume content elements
const previewButton = document.getElementById('toggle-resume-btn');
const resumePreview = document.querySelector('.resume-content');

// Set initial state
if (resumePreview) {
    resumePreview.style.display = 'none';
}

// Add click event listener to the button
if (previewButton) {
    previewButton.addEventListener('click', (event) => {

        // Toggle the visibility
        if (resumePreview.style.display === 'flex') {
            resumePreview.style.display = 'none';
            previewButton.textContent = 'Preview My Resume';
        } else {
            resumePreview.style.display = 'flex';
            previewButton.textContent = 'Hide Preview';
        }
        // Prevent the default link behavior
        event.preventDefault();
    });
}