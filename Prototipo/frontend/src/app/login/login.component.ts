import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { FormsModule } from '@angular/forms';
import { NgIf } from '@angular/common';
import { Router } from '@angular/router';
import { MensajeService } from '../services/mensaje.service';

@Component({
  selector: 'app-login',
  imports: [RouterLink, FormsModule, NgIf],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  correo: string = '';
  password: string = '';
  mensaje: string = '';

  constructor(
    private authService: AuthService,
    private router: Router,
    private mensajeService: MensajeService
  ) {}

  onSubmit() {
    const credentials = {
      correo: this.correo,
      password: this.password,
    };

    this.authService.login(credentials).subscribe({
      next: (response) => {
        this.mensaje = 'Inicio de sesión exitoso';
        console.log(response);
        localStorage.setItem('idUsuario', response.user.id);

        this.mensajeService.setMensaje('Sesión iniciada');

        this.router.navigate(['habitaciones']);
      },
      error: (error) => {
        this.mensaje = 'Error al iniciar sesión';
        console.error(error);
      },
    });
  }
}