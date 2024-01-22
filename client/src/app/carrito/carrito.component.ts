import { Component } from '@angular/core';
import { TiendaService } from '../services/tienda.service';
import { DiscoCarrito } from '../model/discoCarrito';
import { NgFor } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-carrito',
  standalone: true,
  imports: [NgFor],
  templateUrl: './carrito.component.html',
  styleUrl: './carrito.component.css',
})
export class CarritoComponent {
  discosCarrito: DiscoCarrito[] = {} as DiscoCarrito[];

  constructor(private servicioTienda: TiendaService, private router: Router) {}

  ngOnInit(): void {
    this.listarDiscosCarrito();
  }

  listarDiscosCarrito() {
    this.servicioTienda.obtenerDiscosCarrito().subscribe((discosCarrito) => {
      this.discosCarrito = discosCarrito;
    });
  }

  vaciarCarrito() {
    if (
      this.discosCarrito.length == undefined ||
      this.discosCarrito.length == 0
    ) {
      alert('No hay discos en el carrito');
      return;
    }
    this.servicioTienda.vaciarCarrito().subscribe((res) => {
      res == 'ok'
        ? (this.discosCarrito = [])
        : alert('No se puedo vaciar el carrito');
    });
  }

  realizarPedido() {
    if (
      this.discosCarrito.length == undefined ||
      this.discosCarrito.length == 0
    ) {
      alert('No hay discos en el carrito');
      return;
    }
    this.router.navigate(['/pedido']);
  }
}
