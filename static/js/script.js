// Function tied directly to the 'All' button click in subnav
function myFunction() {
    document.getElementById('amazonSidebar').classList.add('open');
    document.getElementById('sidebarOverlay').classList.add('active');
    document.body.classList.add('no-scroll'); // Freezes product grid scrolling behind overlay
}

// Function to close sidebar when clicking X or clicking outside on backdrop tint
function closeSidebar() {
    document.getElementById('amazonSidebar').classList.remove('open');
    document.getElementById('sidebarOverlay').classList.remove('active');
    document.body.classList.remove('no-scroll'); // Restores background scrolling
}
