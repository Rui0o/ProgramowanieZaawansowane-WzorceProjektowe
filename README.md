<h2>Struktura systemu/aplikacji</h2>
<p>Projekt składa się z modułu <code>kreatorPostaci</code>, który zawiera następujące klasy:</p>
<ul>
<li><code>Character</code>: Klasa reprezentująca postać w fikcyjnej grze. Posiada pola:</li>
  <ul>
    <li><code>name</code>: Imię postaci.</li>
    <li><code>hair_color</code>: Kolor włosów postaci.</li>
    <li><code>eye_color</code>: Kolor oczu postaci.</li>
    <li><code>armor</code>: Typ zbroi postaci.</li>
    <li><code>weapon</code>: Typ broni postaci.</li>
  </ul>
<li><code>CharacterBuilder</code>: Klasa odpowiedzialna za budowanie obiektów klasy <code>Character</code>. Udostępnia metody do ustawiania poszczególnych właściwości postaci.</li>
<li><code>CharacterCreator</code>: Klasa, która wykorzystuje <code>CharacterBuilder</code> do tworzenia obiektów klasy <code>Character</code> w bardziej zwięzły sposób.</li>
</ul>
<h2>Scenariusze testów</h2>
<ol>
<li><code>test_character_name</code>: Sprawdza, czy pole <code>name</code> w obiekcie <code>Character</code> jest ustawione poprawnie.</li>
<li><code>test_character_hair_color</code>: Sprawdza, czy pole <code>hair_color</code> w obiekcie <code>Character</code> jest ustawione poprawnie.</li>
<li><code>test_character_eye_color</code>: Sprawdza, czy pole <code>eye_color</code> w obiekcie <code>Character</code> jest ustawione poprawnie.</li>
<li><code>test_character_armor</code>: Sprawdza, czy pole <code>armor</code> w obiekcie <code>Character</code> jest ustawione poprawnie.</li>
<li><code>test_character_weapon</code>: Sprawdza, czy pole <code>weapon</code> w obiekcie <code>Character</code> jest ustawione poprawnie.</li>
<li><code>test_character_creation_and_representation</code>: Sprawdza, czy obiekt <code>Character</code> jest poprawnie tworzony i reprezentowany jako tekst.</li>
<li><code>test_character_creation</code>: Sprawdza, czy obiekt tworzony przez <code>CharacterCreator</code> jest instancją klasy <code>Character</code> i czy pole <code>name</code> jest ustawione poprawnie.</li>
</ol>
<h2>Wykorzystane narzędzia i biblioteki</h2>
<ul>
<li><code>unittest</code>: Biblioteka do tworzenia i uruchamiania testów jednostkowych w Pythonie. Pozwala na definiowanie testów oraz asercji w celu weryfikacji poprawności kodu.</li>
<li>Moduł <code>kreatorPostaci</code>: Własny moduł zdefiniowany przez użytkownika, zawierający klasy i logikę aplikacji.</li>
</ul>
<h2>Ewentualne problemy i ich rozwiązania</h2>
<ul>
<li>Problemy z testami jednostkowymi mogą wynikać z błędów w implementacji klas i metod w module <code>kreatorPostaci</code>. W przypadku wystąpienia błędów, konieczne będzie przejrzenie kodu i zidentyfikowanie ewentualnych niezgodności z oczekiwaniami.</li>
<li>Jeśli testy nie przechodzą, może to oznaczać, że implementacja klas w module <code>kreatorPostaci</code> nie działa poprawnie lub nie zwraca oczekiwanych wartości. W takim przypadku należy przeglądnąć kod i znaleźć miejsce, w którym występuje błąd.</li>
<li>W przypadku wystąpienia błędów składniowych lub zależności brakujących bibliotek, należy sprawdzić poprawność kodu, dostępność wymaganych bibliotek i ich wersji.</li>
</ul>
