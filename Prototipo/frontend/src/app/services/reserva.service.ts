import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReservaService {
  private apiUrl = 'http://127.0.0.1:8000/reservas/';

  constructor(private http: HttpClient) {}

  crearReserva(data: any): Observable<any> {
    return this.http.post(this.apiUrl, data);
  }

  obtenerReservasPorCliente(clienteId: number): Observable<any> {
    return this.http.get(`${this.apiUrl}cliente/${clienteId}`);
  }
}