import { Component, OnInit } from '@angular/core';
import { ReservaService } from '../services/reserva.service';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-mis-reservas',
  imports: [CommonModule, RouterLink],
  templateUrl: './mis-reservas.component.html',
  styleUrl: './mis-reservas.component.css'
})
export class MisReservasComponent implements OnInit {
  reservas: any[] = [];
  clienteId: number | null = null;

  constructor(private reservaService: ReservaService) {}

  ngOnInit() {
    const idUsuario = localStorage.getItem('idUsuario');
    if (idUsuario) {
      this.clienteId = parseInt(idUsuario, 10);
      this.obtenerReservas();
    } else {
      console.error('No se encontró el ID del usuario en localStorage');
    }
  }

  obtenerReservas() {
    if (this.clienteId) {
      this.reservaService.obtenerReservasPorCliente(this.clienteId).subscribe({
        next: (data) => {
          this.reservas = data || [];
          console.log('Reservas obtenidas:', this.reservas);
        },
        error: (error) => {
          console.error('Error al obtener reservas:', error);
          this.reservas = [];
        }
      });
    }
  }
}