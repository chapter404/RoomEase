import { Component, AfterViewInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReservasService } from './reservas.service';

@Component({
  selector: 'app-reservas',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reservas.component.html',
  styleUrls: ['./reservas.component.css']
})
export class ReservasComponent implements AfterViewInit {
  constructor(private reservasService: ReservasService) {}

  ngAfterViewInit(): void {
    const form = document.querySelector('form');
    form?.addEventListener('submit', event => {
      event.preventDefault();
      this.reservar();
    });
  }

  reservar(): void {
    const nombreInput = document.getElementById('nombre') as HTMLInputElement;
    const correoInput = document.getElementById('correo') as HTMLInputElement;
    const fechaInput = document.getElementById('fecha') as HTMLInputElement;
    const habitacionSelect = document.getElementById('habitacion') as HTMLSelectElement;

    const nombre = nombreInput?.value;
    const correo = correoInput?.value;
    const fecha = fechaInput?.value;
    const habitacionValue = habitacionSelect?.value;

    // Mapeo de valores de habitación a IDs
    const mapping: Record<string, number> = {
      individual: 1,
      doble: 2,
      suite: 3
    };
    const habitacionId = mapping[habitacionValue] || 1;

    const datosReserva = {
      nombre,
      correo,
      fechaInicio: fecha,
      fechaFin: fecha,
      habitacionId,
      clienteId: 1 // temporal
    };

    this.reservasService.crearReserva(datosReserva).subscribe({
      next: res => {
        alert('Reserva creada con ID ' + res.reservaId);
      },
      error: err => {
        console.error(err);
        alert('Error al crear reserva');
      }
    });
  }
}
