
const headerMenu=document.querySelector('.hm-header');

console.log(headerMenu.offsetTop);

window.addEventListener('scroll',()=>{
    if(window.pageYOffset > 80){
        headerMenu.classList.add('header-fixed');
    }else{
        headerMenu.classList.remove('header-fixed');
    }
})

/*=========================================
    Tabs
==========================================*/
if(document.querySelector('.hm-tabs')){

    const tabLinks=document.querySelectorAll('.hm-tab-link');
    const tabsContent=document.querySelectorAll('.tabs-content');

    tabLinks[0].classList.add('active');

    if(document.querySelector('.tabs-content')){
        tabsContent[0].classList.add('tab-active');
    }
    

    for (let i = 0; i < tabLinks.length; i++) {
        
        tabLinks[i].addEventListener('click',()=>{

            
            tabLinks.forEach((tab) => tab.classList.remove('active'));
            tabLinks[i].classList.add('active');
            
            tabsContent.forEach((tabCont) => tabCont.classList.remove('tab-active'));
            tabsContent[i].classList.add('tab-active');
            
        });
        
    }

}

/*=========================================
    MENU
==========================================*/

const menu=document.querySelector('.icon-menu');
const menuClose=document.querySelector('.cerrar-menu');

menu.addEventListener('click',()=>{
    document.querySelector('.header-menu-movil').classList.add('active');
})

menuClose.addEventListener('click',()=>{
    document.querySelector('.header-menu-movil').classList.remove('active');
})


// Obtener referencia al botón "Agregar al carrito"
const addToCartButtons = document.querySelectorAll('.hm-btn');

// Agregar evento click a cada botón "Agregar al carrito"
addToCartButtons.forEach(button => {
  button.addEventListener('click', addToCart);
});

// Función para agregar un producto al carrito
function addToCart(event) {
  event.preventDefault();
  const product = event.target.closest('.product-item');

  // Obtener información del producto
  const productName = product.querySelector('h3').innerText;
  const productPrice = product.querySelector('.precio span').innerText;

  // Crear objeto de producto
  const cartItem = {
    name: productName,
    price: productPrice
  };

  // Guardar el producto en el carrito (puedes usar localStorage o una variable global)
  // Por ejemplo, si usas una variable global llamada "cart":
  cart.push(cartItem);

  // Actualizar el número de elementos en el carrito
  updateCartItemCount();
}

// Función para actualizar el número de elementos en el carrito
function updateCartItemCount() {
  const cartItemCount = document.querySelector('.hm-icon-cart span');
  cartItemCount.innerText = cart.length;
}

// Variable global para almacenar los productos del carrito
let cart = [];

