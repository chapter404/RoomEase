import { Component, OnInit } from '@angular/core';
import { RouterLink } from '@angular/router';
import { CommonModule } from '@angular/common';
import { HabitacionesService } from '../services/habitaciones.service';
import { MensajeService } from '../services/mensaje.service';

@Component({
  selector: 'app-habitaciones',
  standalone: true,
  imports: [RouterLink, CommonModule],
  templateUrl: './habitaciones.component.html',
  styleUrl: './habitaciones.component.css'
})
export class HabitacionesComponent implements OnInit {

  habitaciones: any[] = [];
  mensaje: string | null = null;

  constructor(
    private habitacionesService: HabitacionesService,
    private mensajeService: MensajeService
  ) {}

  ngOnInit() {
    this.mensaje = this.mensajeService.getMensaje();
    console.log('Mensaje recibido:', this.mensaje);

    this.habitacionesService.getHabitaciones().subscribe((data) => {
      this.habitaciones = data;
    }, (error) => {
      console.error('Error al obtener habitaciones:', error);
    });
  }
}