import { TestBed } from '@angular/core/testing';

import { FamiliarAsignadoService } from './familiar-asignado.service';

describe('FamiliarAsignadoService', () => {
  let service: FamiliarAsignadoService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FamiliarAsignadoService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
