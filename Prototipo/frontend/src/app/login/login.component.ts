import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { AuthService } from '../services/auth.service';
import { FormsModule } from '@angular/forms';
import { NgIf } from '@angular/common';


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

  constructor(private authService: AuthService) {}

  onSubmit() {
    const credentials = {
      correo: this.correo,
      password: this.password,
    };

    this.authService.login(credentials).subscribe({
      next: (response) => {
        this.mensaje = 'Inicio de sesión exitoso';
        console.log(response);
      },
      error: (error) => {
        this.mensaje = 'Error al iniciar sesión';
        console.error(error);
      },
    });
  }
}