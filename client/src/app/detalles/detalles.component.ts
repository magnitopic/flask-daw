import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TiendaService } from '../services/tienda.service';
import { Disco } from '../model/disco';

@Component({
  selector: 'app-detalles',
  standalone: true,
  imports: [],
  templateUrl: './detalles.component.html',
  styleUrl: './detalles.component.css',
})
export class DetallesComponent {
  id_disco: number = 0;
  disco: Disco = {} as Disco;

  constructor(
    private servicioTienda: TiendaService,
    private activatedRoute: ActivatedRoute
  ) {}

  ngOnInit(): void {
    this.id_disco = Number(this.activatedRoute.snapshot.paramMap.get('id'));
    this.servicioTienda.obtenerDiscoPorId(this.id_disco).subscribe((disco) => {
      this.disco = disco;
      this.disco.fecha = this.disco.fecha?.replace('00:00:00 GMT', '');
    });
  }

  agregar_producto_al_carrito() {
    this.servicioTienda.agregarAlCarrito(this.id_disco, 1).subscribe((res) => {
      res == 'ok'
        ? alert('Producto agregado al carrito')
        : alert('Error al agregar el producto al carrito');
    });
  }
}
