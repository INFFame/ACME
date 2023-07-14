function eliminarProducto(event, codigo) {
    event.preventDefault();
    
    Swal.fire({
      title: '¿Seguro que quieres eliminarlo?',
      text: '¡No podrás deshacer esto!',
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Sí, bórralo'
    }).then((result) => {
      if (result.isConfirmed) {
        window.location.href = '/eliminar-producto/' + codigo + '/';
      }
    });
  }