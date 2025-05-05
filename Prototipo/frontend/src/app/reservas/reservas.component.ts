import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { ReservaService } from '../services/reserva.service';

@Component({
  selector: 'app-reservas',
  standalone: true,
  imports: [CommonModule, RouterLink],
  templateUrl: './reservas.component.html',
  styleUrls: ['./reservas.component.css']
})
export class ReservasComponent {
  constructor(private reservaService: ReservaService) {}

  reservar(event: Event): void {
    event.preventDefault();

    const nombreInput    = document.getElementById('nombre')     as HTMLInputElement;
    const correoInput    = document.getElementById('correo')     as HTMLInputElement;
    const fechaInput     = document.getElementById('fecha')      as HTMLInputElement;
    const habitacionSel  = document.getElementById('habitacion') as HTMLSelectElement;

    const fecha          = fechaInput.value;
    const habitacionValue= habitacionSel.value;

    const mapping: Record<string,number> = {
      individual: 1, doble: 2, suite: 3
    };
    const habitacionId = mapping[habitacionValue] || 1;

    const clienteId = localStorage.getItem('idUsuario');
    if (!clienteId) {
      alert('No se encontró el ID del cliente. Por favor, inicia sesión.');
      return;
    }

    const datosReserva = {
      fechaInicio: fecha,
      fechaFin:    fecha,
      habitacionId,
      clienteId:   parseInt(clienteId, 10)
    };

    this.reservaService.crearReserva(datosReserva).subscribe({
      next: res  => alert('Reserva creada con ID ' + res.reservaId),
      error: err => { console.error(err); alert('Error al crear reserva'); }
    });
  }
}
