import { Component } from '@angular/core';
import { TiendaService } from '../services/tienda.service';
import { Disco } from '../model/disco';
import { NgFor } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-listado',
  standalone: true,
  imports: [NgFor],
  templateUrl: './listado.component.html',
  styleUrls: ['./listado.component.css'],
})
export class ListadoComponent {
  discos: Disco[] = {} as Disco[];
  constructor(private servicioTienda: TiendaService, private router:Router) {}

  ngOnInit(): void {
    this.servicioTienda.obtenerDiscos().subscribe((data) => {
      this.discos = data;
    });
  }

  verDetalles(d: Disco) {
    
    this.router.navigate(['/detalles', d.id]);
  }
}
