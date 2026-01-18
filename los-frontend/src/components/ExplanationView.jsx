// src/components/ExplanationView.jsx

import ShapChart from "./ShapChart";

function parseExplanation(text) {
  const summaryMatch = text.match(/CLINICAL_SUMMARY:\n([\s\S]*?)\n\nRECOMMENDATION:/);
  const recMatch = text.match(/RECOMMENDATION:\n([\s\S]*)$/);

  const summary = summaryMatch
    ? summaryMatch[1].split("\n").filter(l => l.startsWith("-"))
    : [];

  const recommendation = recMatch
    ? recMatch[1].split("\n").filter(l => l.startsWith("-"))
    : [];

  return { summary, recommendation };
}

export default function ExplanationView({ result }) {
  const { summary, recommendation } = parseExplanation(result.explanation);

  return (
    <div className="card full center">
      <h2>🩺 Clinical Explanation</h2>
      <p className="subtitle">Model-driven reasoning & feature contribution</p>

      {/* SHAP */}
      {result?.shap?.length > 0 && (
        <div className="shap-container">
          <ShapChart data={result.shap} />
        </div>
      )}

      {/* TWO COLUMN EXPLANATION */}
      <div className="explain-grid">
        <div className="explain-box">
          <h3>📋 Clinical Summary</h3>
          <ul>
            {summary.map((item, i) => (
              <li key={i}>{item.replace("-", "").trim()}</li>
            ))}
          </ul>
        </div>

        <div className="explain-box">
          <h3>🩺 Recommendation</h3>
          <ul>
            {recommendation.map((item, i) => (
              <li key={i}>{item.replace("-", "").trim()}</li>
            ))}
          </ul>
        </div>
      </div>
    </div>
  );
}
