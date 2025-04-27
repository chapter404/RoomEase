import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-crear-habitacion',
  imports: [RouterLink, FormsModule],
  templateUrl: './crear-habitacion.component.html',
  styleUrl: './crear-habitacion.component.css'
})

export class CrearHabitacionComponent {
  habitacion = {
    numero: '',
    tipo: '',
    precio: 0,
    estado: 'disponible',
    descripcion: ''
  };
  fotos: File[] = [];

  constructor(private http: HttpClient) {}

  onFileChange(event: any): void {
    if (event.target.files && event.target.files.length > 0) {
      this.fotos = Array.from(event.target.files);
    }
  }

  onSubmit(): void {
    const formData = new FormData();

    formData.append('numero', this.habitacion.numero);
    formData.append('tipo', this.habitacion.tipo);
    formData.append('precio', this.habitacion.precio.toString());
    formData.append('estado', this.habitacion.estado);
    formData.append('descripcion', this.habitacion.descripcion);

    this.fotos.forEach((foto, index) => {
      formData.append(`fotos`, foto, foto.name);
    });

    this.http.post('http://localhost:8000/habitaciones/', formData).subscribe({
      next: (response) => {
        console.log('Habitación creada:', response);
      },
      error: (error) => {
        console.error('Error al crear la habitación: ', error);
      }
    });
  }
}