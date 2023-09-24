const fileUpload = document.getElementById('file-upload');
const fileLabel = document.getElementById('file-label');

document.addEventListener('dragover', function (e) {
    e.preventDefault();
    fileLabel.classList.add('dragover');
});

document.addEventListener('dragleave', function () {
    fileLabel.classList.remove('dragover');
});

document.addEventListener('drop', function (e) {
    e.preventDefault();
    fileLabel.classList.remove('dragover');

    const file = e.dataTransfer.files[0];

    if (file) {
        const fileName = file.name;
        document.getElementById('file-name').textContent = fileName;
        fileUpload.files = e.dataTransfer.files;
    }
});

fileUpload.addEventListener('change', function (e) {
    const file = e.target.files[0];

    if (file) {
        const fileName = file.name;
        document.getElementById('file-name').textContent = fileName;
    }
});
