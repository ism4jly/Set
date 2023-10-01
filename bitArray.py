class BitSet:
  def __init__(self, size):
      self.size = size
      self.bits = [False] * size

  def add(self, num):
      if num < 0 or num >= self.size:
        raise ValueError("Elemento fora de alcance")
      self.bits[num] = True

  def remove(self, num):
      if num < 0 or num >= self.size:
        raise ValueError("Elemento fora de alcance")
      self.bits[num] = False

  def contains(self, num):
      if num < 0 or num >= self.size:
        raise ValueError("Elemento fora de alcance")
      return self.bits[num]

  def union(self, other_set):
      if self.size != other_set.size:
        raise ValueError("Os conjuntos devem ter o mesmo tamanho para a operação de união")
      resultado = BitSet(self.size)
      for i in range(self.size):
        resultado.bits[i] = self.bits[i] or other_set.bits[i]
      return resultado

  def intersection(self, other_set):
      if self.size != other_set.size:
        raise ValueError("Os conjuntos devem ter o mesmo tamanho para a operação de interseção")
      resultado = BitSet(self.size)
      for i in range(self.size):
        resultado.bits[i] = self.bits[i] and other_set.bits[i]
      return resultado

  def difference(self, other_set):
      if self.size != other_set.size:
        raise ValueError("Os conjuntos devem ter o mesmo tamanho para a operação de diferença")
      resultado = BitSet(self.size)
      for i in range(self.size):
        resultado.bits[i] = self.bits[i] and not other_set.bits[i]
      return resultado

  def __str__(self):
    return "{" + ", ".join(str(i) for i in range(self.size) if self.bits[i]) + "}"

