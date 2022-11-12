import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CrearRegistroSignosVitalesComponent } from './crear-registro-signos-vitales.component';

describe('CrearRegistroSignosVitalesComponent', () => {
  let component: CrearRegistroSignosVitalesComponent;
  let fixture: ComponentFixture<CrearRegistroSignosVitalesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CrearRegistroSignosVitalesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CrearRegistroSignosVitalesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
