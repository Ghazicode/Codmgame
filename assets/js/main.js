// Functionality for search input
document.addEventListener('DOMContentLoaded', function() {
    const searchIcon = document.querySelector('.search-icon');
    const searchInputContainer = document.querySelector('.search-input-container');

    // Create and append the search input to the container
    const searchInput = document.createElement('input');
    searchInput.setAttribute('type', 'text');
    searchInput.setAttribute('placeholder', 'جستجو...');
    searchInput.className = 'form-control rounded-pill';
    searchInputContainer.appendChild(searchInput);

    searchIcon.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent default link behavior
        searchInputContainer.classList.toggle('active');
        if (searchInputContainer.classList.contains('active')) {
            searchInput.focus(); // Focus on the input when it becomes active
        }
    });
});

