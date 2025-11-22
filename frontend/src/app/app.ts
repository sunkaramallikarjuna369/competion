import { Component, signal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { timeout, finalize } from 'rxjs';

interface SimplifyResponse {
  original_text: string;
  simplified_text: string;
  level: string;
  word_count_original: number;
  word_count_simplified: number;
  reading_level: string;
}

@Component({
  selector: 'app-root',
  imports: [CommonModule, FormsModule, HttpClientModule],
  templateUrl: './app.html',
  styleUrls: ['./app.css']
})
export class App {
  protected readonly title = signal('Accessibility Text Simplifier');
  
  inputText = '';
  simplifiedText = '';
  selectedLevel = 'intermediate';
  isLoading = false;
  error = '';
  showResult = false;
  
  wordCountOriginal = 0;
  wordCountSimplified = 0;
  readingLevel = '';
  
  private apiUrl = 'https://app-ztsetvxb.fly.dev';
  
  levels = [
    { value: 'basic', label: 'Basic', description: 'Elementary (Ages 8-10)' },
    { value: 'intermediate', label: 'Intermediate', description: 'Middle School (Ages 11-14)' },
    { value: 'advanced', label: 'Advanced', description: 'High School (Ages 15-18)' }
  ];
  
  exampleTexts = [
    {
      title: 'Legal Text',
      text: 'The party of the first part hereby agrees to indemnify and hold harmless the party of the second part from any and all claims, damages, losses, and expenses, including but not limited to reasonable attorneys\' fees, arising out of or resulting from the performance of this agreement.'
    },
    {
      title: 'Medical Text',
      text: 'The patient presents with acute myocardial infarction characterized by substernal chest pain radiating to the left arm, accompanied by diaphoresis and dyspnea. Electrocardiogram reveals ST-segment elevation in leads II, III, and aVF, consistent with inferior wall myocardial infarction.'
    },
    {
      title: 'Technical Text',
      text: 'The algorithm utilizes a convolutional neural network architecture with multiple layers of feature extraction, employing rectified linear unit activation functions and dropout regularization to mitigate overfitting while optimizing the loss function through stochastic gradient descent.'
    }
  ];
  
  constructor(private http: HttpClient) {}
  
  simplifyText() {
    if (!this.inputText.trim()) {
      this.error = 'Please enter some text to simplify';
      return;
    }
    
    this.isLoading = true;
    this.error = '';
    this.showResult = false;
    
    this.http.post<SimplifyResponse>(
      `${this.apiUrl}/api/simplify`,
      {
        text: this.inputText,
        level: this.selectedLevel
      }
    )
    .pipe(
      timeout(20000),
      finalize(() => {
        this.isLoading = false;
      })
    )
    .subscribe({
      next: (response) => {
        this.simplifiedText = response.simplified_text;
        this.wordCountOriginal = response.word_count_original;
        this.wordCountSimplified = response.word_count_simplified;
        this.readingLevel = response.reading_level;
        this.showResult = true;
      },
      error: (err: any) => {
        this.error = err?.error?.detail || 'Failed to simplify text. Please check if the backend is running and OpenAI API key is configured.';
        console.error('Error:', err);
      }
    });
  }
  
  loadExample(example: any) {
    this.inputText = example.text;
    this.showResult = false;
    this.error = '';
  }
  
  clearText() {
    this.inputText = '';
    this.simplifiedText = '';
    this.showResult = false;
    this.error = '';
  }
  
  copyToClipboard(text: string) {
    navigator.clipboard.writeText(text).then(() => {
      alert('Text copied to clipboard!');
    });
  }
}
