import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { FormsModule } from '@angular/forms';
import { NgIf } from '@angular/common';


@Component({
  selector: 'app-registro',
  imports: [RouterLink, FormsModule, NgIf],
  templateUrl: './registro.component.html',
  styleUrl: './registro.component.css'
})
export class RegistroComponent {
  nombre: string = '';
  correo: string = '';
  password: string = '';
  rut: string = '';
  dv: string = '';
  telefono: string = '';
  mensaje: string = '';

  constructor(private authService: AuthService) {}

  onSubmit() {
    const user = {
      nombre: this.nombre,
      correo: this.correo,
      password: this.password,
      rut: parseInt(this.rut),
      dv: this.dv,
      telefono: parseInt(this.telefono),
    };

    this.authService.register(user).subscribe({
      next: (response) => {
        this.mensaje = 'Usuario registrado con éxito';
        console.log(response);
      },
      error: (error) => {
        this.mensaje = 'Error al registrar el usuario';
        console.error(error);
      },
    });
  }
}