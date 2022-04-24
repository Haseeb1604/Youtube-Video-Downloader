let menu_btn = document.querySelector("#menu-btn");
let sidebar = document.querySelector("#sidebar");
let container = document.querySelector(".my-container");

menu_btn.addEventListener("click", () => {
  sidebar.classList.toggle("active-nav");
  container.classList.toggle("active-cont");
});
