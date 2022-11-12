import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class FamiliarAsignadoService {
  env: String;
  constructor(private _httpClient: HttpClient) { 
    this.env = environment.app_url;
  }
  obtenerFamiliar(id: any){
    return this._httpClient.get<any>(`${this.env}/familiar/consultar/${id}/`);
  }
  crearFamiliar(data: any){
    return this._httpClient.post<any>(`${this.env}/familiar/registrar/`, data);
  }
}
