// // Frontend integration script for ModelProof
// // Uses existing UI handlers and adds a backend search integration.

// const API_URL = "http://127.0.0.1:8000/recommend"; // override with full URL in production, e.g. https://your-backend.onrender.com/recommend

// function escapeHtml(str){
//   return String(str)
//     .replace(/&/g, "&amp;")
//     .replace(/</g, "&lt;")
//     .replace(/>/g, "&gt;")
//     .replace(/"/g, "&quot;")
//     .replace(/'/g, "&#39;");
// }

// async function searchBackend(query, top_k=5){
//   const payload = { query, top_k };
//   const res = await fetch(API_URL, {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify(payload)
//   });
//   if(!res.ok){
//     const text = await res.text();
//     throw new Error(`Search failed: ${res.status} ${text}`);
//   }
//   return res.json();
// }

// // Small modal helper reuse — this file expects the same modal elements from your HTML.
// function showSearchResults(result) {

//   const modal = document.getElementById("modal");
//   const modalTitle = document.getElementById("modalTitle");
//   const modalText = document.getElementById("modalText");

//   modalTitle.textContent = `Results: ${result.query}`;

//   let html = "";

//   // Parsed requirement
//   if (result.parsed_requirement) {
//     const req = result.parsed_requirement;

//     html += `
//       <h3>Requirement</h3>
//       <p>
//         <strong>Task:</strong> ${escapeHtml(req.task || "Not specified")}<br>
//         <strong>Languages:</strong> ${escapeHtml(
//           (req.languages || []).join(", ") || "Not specified"
//         )}
//       </p>
//     `;
//   }

//   // ONLY filtered candidates
//   const models = result.filtered_models || [];

//   if (models.length) {

//     html += `<h3>Matching Models</h3>`;

//     models.forEach((m) => {

//       const name = escapeHtml(
//         m.metadata?.model_name ||
//         m.metadata?.model ||
//         "Unknown Model"
//       );

//       const task = escapeHtml(
//         m.metadata?.task || "Not specified"
//       );

//       const languages = escapeHtml(
//         m.metadata?.supported_languages ||
//         "Not specified"
//       );

//       const score = m.relevance_score ?? "";

//       const source = escapeHtml(
//         m.metadata?.documentation_url ||
//         m.metadata?.model_card_url ||
//         ""
//       );

//       html += `
//         <div class="model-result">

//           <h4>${name}</h4>

//           <p>
//             <strong>Task:</strong> ${task}<br>
//             <strong>Languages:</strong> ${languages}<br>
//             <strong>Relevance:</strong> ${score}
//           </p>

//           ${
//             source
//               ? `<a href="${source}" target="_blank">
//                    View Model
//                  </a>`
//               : ""
//           }

//         </div>
//       `;
//     });

//   } else {

//     html += `
//       <h3>No matching models found</h3>
//       <p>
//         No model in the current knowledge base satisfies
//         the requested requirements.
//       </p>
//     `;
//   }

//   modalText.innerHTML = html;

//   modal.classList.add("show");
//   document.body.style.overflow = "hidden";
// }
//  html += `<li><strong>${name}</strong> — relevance: ${relevance}<br>${snippet}${source?`<br><a href="${source}" target="_blank">source</a>`:''}</li>`;
// }
//     html += `</ul>`;
//   }
//   modalText.innerHTML = html || 'No results';
//   modal.classList.add('show');
//   document.body.style.overflow = 'hidden';
// }

// function showError(err){
//   const modal=document.getElementById("modal");
//   const modalTitle=document.getElementById("modalTitle");
//   const modalText=document.getElementById("modalText");
//   modalTitle.textContent = 'Error';
//   modalText.textContent = err.message || String(err);
//   modal.classList.add('show');
//   document.body.style.overflow = 'hidden';
// }

// // Attach Enter key to the existing search input (if present in your full HTML)
// document.addEventListener('DOMContentLoaded', ()=>{
//   const searchInput = document.getElementById('modelSearch');
//   if(!searchInput) return;
//   searchInput.addEventListener('keydown', async (e)=>{
//     if(e.key === 'Enter'){
//       const q = searchInput.value.trim();
//       if(!q) return;
//       try{
//         // show loading
//         const modal=document.getElementById("modal");
//         const modalTitle=document.getElementById("modalTitle");
//         const modalText=document.getElementById("modalText");
//         modalTitle.textContent = 'Searching...';
//         modalText.textContent = 'Please wait — querying the ModelProof backend.';
//         modal.classList.add('show');
//         document.body.style.overflow = 'hidden';

//         const result = await searchBackend(q, 5);
//         showSearchResults(result);
//       }catch(err){
//         showError(err);
//       }
//     }
//   });
// });


// ============================================================
// ModelProof - Frontend ↔ Backend Integration
// ============================================================

// Local backend during development
const API_URL = window.API_URL || "http://127.0.0.1:8000/recommend";


// ============================================================
// Security helper
// ============================================================

function escapeHtml(str) {
  return String(str ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}


// ============================================================
// Call ModelProof Backend
// ============================================================

async function searchBackend(query, top_k = 5) {

  const payload = {
    query: query,
    top_k: top_k
  };

  const response = await fetch(API_URL, {
    method: "POST",

    headers: {
      "Content-Type": "application/json"
    },

    body: JSON.stringify(payload)
  });

  if (!response.ok) {

    const text = await response.text();

    throw new Error(
      `Search failed (${response.status}): ${text}`
    );
  }

  return await response.json();
}


// ============================================================
// Display Search Results
// ============================================================

function showSearchResults(result) {

  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modalTitle");
  const modalText = document.getElementById("modalText");

  if (!modal || !modalTitle || !modalText) {
    console.error(
      "Modal elements not found. Check modal, modalTitle and modalText IDs."
    );
    return;
  }

  modalTitle.textContent = `Results: ${result.query}`;

  let html = "";


  // ==========================================================
  // Parsed Requirement
  // ==========================================================

  if (result.parsed_requirement) {

    const requirement = result.parsed_requirement;

    const task =
      requirement.task || "Not specified";

    const languages =
      Array.isArray(requirement.languages)
        ? requirement.languages.join(", ")
        : "Not specified";

    html += `
      <div class="requirement-result">

        <h3>Requirement</h3>

        <p>
          <strong>Task:</strong>
          ${escapeHtml(task)}
        </p>

        <p>
          <strong>Languages:</strong>
          ${escapeHtml(languages)}
        </p>

      </div>
    `;
  }


  // ==========================================================
  // FILTERED MODELS
  // ==========================================================
  // IMPORTANT:
  // We display filtered_models, NOT retrieved_models.
  // ==========================================================

  const models = result.filtered_models || [];

  if (models.length > 0) {

    html += `
      <div class="matching-models">

        <h3>Matching Models</h3>
    `;


    models.forEach((model) => {

      const metadata = model.metadata || {};

      const modelName =
        metadata.model_name ||
        metadata.model ||
        "Unknown Model";

      const task =
        metadata.task ||
        "Not specified";

      const languages =
        metadata.supported_languages ||
        "Not specified";

      const relevance =
        model.relevance_score !== undefined
          ? model.relevance_score
          : "N/A";


      // Source URL
      const source =
        metadata.documentation_url ||
        metadata.model_card_url ||
        "";


      html += `
        <div class="model-result">

          <h4>
            ${escapeHtml(modelName)}
          </h4>

          <p>
            <strong>Task:</strong>
            ${escapeHtml(task)}
          </p>

          <p>
            <strong>Languages:</strong>
            ${escapeHtml(languages)}
          </p>

          <p>
            <strong>Relevance:</strong>
            ${escapeHtml(relevance)}
          </p>

          ${
            source
              ? `
                <p>
                  <a
                    href="${escapeHtml(source)}"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    View Model Source
                  </a>
                </p>
              `
              : ""
          }

        </div>
      `;
    });


    html += `
      </div>
    `;

  } else {

    // ========================================================
    // No candidates
    // ========================================================

    html += `
      <div class="no-results">

        <h3>No Matching Models Found</h3>

        <p>
          No model in the current knowledge base
          satisfies the requested requirements.
        </p>

      </div>
    `;
  }


  // ==========================================================
  // Backend Answer
  // ==========================================================
  // Currently your LLM is not configured, so we don't make
  // "LLM generation is not configured yet." the main result.
  // ==========================================================

  if (
    result.answer &&
    !result.answer.includes("LLM generation is not configured yet")
  ) {

    html += `
      <div class="ai-answer">

        <h3>AI Recommendation</h3>

        <p>
          ${escapeHtml(result.answer)}
        </p>

      </div>
    `;
  }


  // Put content inside modal
  modalText.innerHTML = html || "No results found.";

  modal.classList.add("show");

  document.body.style.overflow = "hidden";
}


// ============================================================
// Error Display
// ============================================================

function showError(error) {

  const modal = document.getElementById("modal");
  const modalTitle = document.getElementById("modalTitle");
  const modalText = document.getElementById("modalText");

  if (!modal || !modalTitle || !modalText) {

    console.error(error);

    return;
  }

  modalTitle.textContent = "Error";

  modalText.textContent =
    error?.message ||
    "Something went wrong while searching.";

  modal.classList.add("show");

  document.body.style.overflow = "hidden";
}


// ============================================================
// Search Input
// ============================================================

document.addEventListener("DOMContentLoaded", () => {

  const searchInput =
    document.getElementById("modelSearch");


  if (!searchInput) {

    console.error(
      "Search input with id='modelSearch' was not found."
    );

    return;
  }


  // ==========================================================
  // Press ENTER to search
  // ==========================================================

  searchInput.addEventListener("keydown", async (event) => {

    if (event.key !== "Enter") {
      return;
    }

    const query =
      searchInput.value.trim();


    if (!query) {
      return;
    }


    // ========================================================
    // Show loading
    // ========================================================

    const modal =
      document.getElementById("modal");

    const modalTitle =
      document.getElementById("modalTitle");

    const modalText =
      document.getElementById("modalText");


    if (modal && modalTitle && modalText) {

      modalTitle.textContent = "Searching...";

      modalText.textContent =
        "Please wait — ModelProof is finding matching models.";

      modal.classList.add("show");

      document.body.style.overflow = "hidden";
    }


    // ========================================================
    // Backend request
    // ========================================================

    try {

      const result =
        await searchBackend(query, 5);

      console.log(
        "ModelProof backend response:",
        result
      );

      showSearchResults(result);

    } catch (error) {

      console.error(
        "ModelProof search error:",
        error
      );

      showError(error);
    }

  });

});
