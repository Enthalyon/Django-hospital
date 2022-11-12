import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class SignosVitalesService {
  env: String;
  constructor(private _httpClient: HttpClient) { 
    this.env = environment.app_url;
  }
  crearSignos(data: any){
    return this._httpClient.post(`${this.env}/vitalidad/registrar/`, data)
  }
  consultarSignosPorPaciente(id: any){
    return this._httpClient.get(`${this.env}/vitalidad/consultar/paciente/${id}/`)
  }
  actualizarSignos(id: any, data: any){
    return this._httpClient.put(`${this.env}/vitalidad/actualizar/${id}/`, data)
  }
}
