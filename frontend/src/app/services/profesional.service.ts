import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ProfesionalService {
  env: String;
  constructor(private _httpClient: HttpClient) { 
    this.env = environment.app_url;
  }
  obtenerProfesional(id: any){
    return this._httpClient.get<any>(`${this.env}/profesional/consultar/${id}/`);
  }
  crearProfesional(data: any){
    return this._httpClient.post<any>(`${this.env}/profesional/registrar/`, data);
  }
  listarProfesionales(){
    return this._httpClient.get<any>(`${this.env}/profesionales/consultar/`);
  }
}
