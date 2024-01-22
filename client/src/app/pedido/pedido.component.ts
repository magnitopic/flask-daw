import { Component } from '@angular/core';
import { Pedido } from '../model/pedido';
import { FormsModule } from '@angular/forms';
import { TiendaService } from '../services/tienda.service';
import { Router } from '@angular/router';
import { Validator } from '../validaciones/validator';

@Component({
  selector: 'app-pedido',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './pedido.component.html',
  styleUrl: './pedido.component.css',
})
export class PedidoComponent {
  pedido: Pedido = {} as Pedido;

  constructor(
    private validador: Validator,
    private servicioTienda: TiendaService,
    private router: Router
  ) {}

  finalizarPedido() {
    //validar la info del pedido    
    if (!this.validador.validarNombre(this.pedido.nombre)) {
      alert('Nombre incorrecto');
      return;
    }
    if (!this.validador.validarEmail(this.pedido.email)) {
      alert('Email incorrecto');
      return;
    }
    if (!this.validador.validarDireccion(this.pedido.direccion)) {
      alert('Direccion incorrecta');
      return;
    }
    if (!this.validador.validarTelefono(this.pedido.telefono)) {
      alert('Telefono incorrecto');
      return;
    }
    if (!this.validador.validarTarjeta(this.pedido.tarjeta)) {
      alert('Tarjeta incorrecta');
      return;
    }
    if (!this.validador.validarCaducidad(this.pedido.caducidad)) {
      alert('Caducidad incorrecta');
      return;
    }
    if (!this.validador.validarCVV(this.pedido.cvv)) {
      alert('CVV incorrecto');
      return;
    }

    this.servicioTienda
      .registrarPedido(this.pedido)
      .subscribe((res) =>
        res == 'ok' ? this.pedidoOK() : alert('Error al registrar el pedido')
      );
  }
  pedidoOK() {
    alert('Pedido realizado correctamente');
    this.router.navigate(['listado']);
  }
}
