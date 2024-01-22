import { Injectable } from '@angular/core';
@Injectable({
  providedIn: 'root',
})
export class Validator {
  regexp_nombre: RegExp = /^[a-z áéíóúñ]{2,10}$/i;
  regexp_email: RegExp = /^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$/i;
  regexp_direccion: RegExp = /^[a-z0-9 áéíóúñ\\/:ºª]{2,50}$/i;
  regexp_telefono: RegExp = /^[0-9]{9}$/;
  regexp_tarjeta: RegExp = /^[0-9]{16}$/;
  regexp_caducidad: RegExp = /^[0-9]{2}\/[0-9]{2}$/;
  regexp_cvv: RegExp = /^[0-9]{3}$/;

  validarNombre(nombre: string): boolean {
    return this.regexp_nombre.test(nombre) || (nombre != undefined);
  }

  validarDireccion(direccion: string): boolean {
    return this.regexp_direccion.test(direccion) && (direccion != undefined);
  }

  validarTarjeta(tarjeta: string): boolean {
    return this.regexp_tarjeta.test(tarjeta) || (tarjeta != undefined);
  }

  validarCaducidad(caducidad: string): boolean {
    return this.regexp_caducidad.test(caducidad) || (caducidad != undefined);
  }

  validarCVV(cvv: string): boolean {
    return this.regexp_cvv.test(cvv) || (cvv != undefined);
  }

  validarEmail(email: string): boolean {
    return this.regexp_email.test(email) || (email != undefined);
  }

  validarTelefono(telefono: string): boolean {
    return this.regexp_telefono.test(telefono) || (telefono != undefined);
  }
}
