const resource = document.querySelectorAll(".resource-list-object");
const modal = document.querySelector(".modal");

function toggleModal() {
  modal.classList.toggle("show-modal");
}

function windowOnClick(event) {
  if (event.target === modal) {
    toggleModal();
  }
}


const show_resource_details = async (resource_type, resource_id, resource_title) => {
  console.log(resource_type);
  console.log(resource_id);
  const modal_title = document.querySelector("#modal-title");
  const modal_stock_count = document.querySelector("#modal-stock-count");
  const modal_cost_per_unit = document.querySelector("#modal-cost-per-unit");
  const modal_order_quantity = document.querySelector("#modal-order-quantity");
  const modal_order_cost = document.querySelector("#pricing-estimate");


  // Title & Author Name
  const author_name = "(" + resource_title.split(", ")[1].trim() + ")";
  modal_title.textContent = resource_title.split(", ")[0] + " " + author_name;


  // Stock Count
  const content = await fetch("/" + resource_type + "/" + resource_id + "/");
  resource_object = await content.json();
  modal_stock_count.textContent = "Stock count: " + resource_object['stock_count'];
  modal_cost_per_unit.textContent = "Cost per unit: ₦" + Number(resource_object['cost_per_unit']).toLocaleString();

  // Order Quantity Input
  modal_order_quantity.setAttribute("max", resource_object['stock_count']);

  // Event Listener On Update Of Order Quantity Input
  modal_order_quantity.addEventListener('input', (e) => {
    console.log('change happened here!');
    console.log(modal_order_quantity.value);
    if (modal_order_quantity.value > Number(modal_order_quantity.max)) {
      alert("Stock quantity exceeded.");
      modal_order_quantity.value = Number(modal_order_quantity.max);
    }
    modal_order_cost.textContent = "Order Cost: ₦" + (modal_order_quantity.value * Number(modal_cost_per_unit.textContent.substring(16).replaceAll(",", ""))).toLocaleString();

  })

  modal.classList.add("show-modal");
  const order_now_button = document.querySelector(".order-now-button");

  // Event listener for the order now button
  if (order_now_button) {
    order_now_button.addEventListener("click", () => {
      // console.log("chick lol");
      // window.location.assign("/" + resource_type + "/" + resource_id + "/");
      alert("Your order has been placed successfully!");
    })
  }


}


window.addEventListener("click", windowOnClick);

resource.forEach(b => {
  b.addEventListener('click', () => {
    var res_det = b.getAttribute('data-resource_detail');
    show_resource_details(res_det.split(" ")[0], res_det.split(" ")[2], b.textContent);
  })
})