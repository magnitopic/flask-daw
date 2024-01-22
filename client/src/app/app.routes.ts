import { Routes } from '@angular/router';
import { ListadoComponent } from './listado/listado.component';
import { DetallesComponent } from './detalles/detalles.component';
import { CarritoComponent } from './carrito/carrito.component';
import { PedidoComponent } from './pedido/pedido.component';

export const routes: Routes = [
  { path: 'listado', component: ListadoComponent },
  { path: 'carrito', component: CarritoComponent },
  { path: 'detalles/:id', component: DetallesComponent },
  { path: 'pedido', component: PedidoComponent },
];
