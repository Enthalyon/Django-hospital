import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class PacienteService {
  env: String;
  constructor(private _httpClient: HttpClient) { 
    this.env = environment.app_url;
  }
  obtenerPaciente(id: any){
    return this._httpClient.get<any>(`${this.env}/paciente/consultar/${id}/`);
  }
  obtenerPacientePorId(id: any){
    return this._httpClient.get<any>(`${this.env}/paciente/obtener/${id}/`);
  }
  crearPaciente(data: any){
    return this._httpClient.post<any>(`${this.env}/paciente/registrar/`, data);
  }
  actualizarPaciente(data: any, id: any){
    return this._httpClient.put<any>(`${this.env}/paciente/actualizar/${id}/`, data);
  }
  obtenerPacientesPorProfesional(id: any){
    return this._httpClient.get<any>(`${this.env}/pacientes/consultar/profesional/${id}/`);
  }
  obtenerPacientesPorFamiliar(id: any){
    return this._httpClient.get<any>(`${this.env}/pacientes/consultar/familiar/${id}/`);
  }
  obtenerTodosLosPacientes(){
    return this._httpClient.get<any>(`${this.env}/pacientes/consultar/`);
  }
}
