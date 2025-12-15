import { projects } from './config.js';

// Render projects
function renderProjects() {
  const projectsList = document.getElementById('projects-list');
  const projectsCount = document.getElementById('projects-count');
  
  if (!projectsList) return;
  
  projectsCount.textContent = projects.length;
  
  projectsList.innerHTML = projects.map((project, index) => {
    if (project.link) {
      return `
        <div
          class="group hover:bg-gray-800/50 p-1 rounded transition-colors"
          role="listitem"
        >
          <a
            href="${project.link}"
            target="_blank"
            rel="noopener noreferrer"
            class="block focus:outline-none focus:ring-2 focus:ring-cyan-600 focus:ring-offset-2 focus:ring-offset-gray-900 rounded"
            aria-label="Visit ${project.title}: ${project.description}"
          >
            <div class="flex items-start gap-2">
              <span
                class="text-gray-400 w-6 shrink-0"
                aria-hidden="true"
              >
                ${String(index + 1).padStart(2, "0")}.
              </span>
              <span
                class="text-yellow-360 shrink-0"
                role="img"
                aria-label="Project icon"
              >
                ${project.icon}
              </span>
              <div class="min-w-0 flex-1">
                <span class="text-white group-hover:text-cyan-300 font-semibold">
                  ${project.title}
                </span>
                <span class="text-gray-500 ml-2">
                  → ${project.description}
                </span>
              </div>
            </div>
          </a>
        </div>
      `;
    } else {
      return `
        <div
          class="flex items-start gap-2 opacity-60"
          aria-label="${project.title}: ${project.description} (Coming soon)"
        >
          <span class="text-gray-400 w-6 shrink-0" aria-hidden="true">
            ${String(index + 1).padStart(2, "0")}.
          </span>
          <span
            class="text-yellow-360 shrink-0"
            role="img"
            aria-label="Project icon"
          >
            ${project.icon}
          </span>
          <div class="min-w-0 flex-1">
            <span class="text-white font-semibold">
              ${project.title}
            </span>
            <span class="text-gray-500 ml-2">
              → ${project.description}
            </span>
            <span class="text-gray-600 ml-2">[coming soon]</span>
          </div>
        </div>
      `;
    }
  }).join('');
}


// Initialize page
document.addEventListener('DOMContentLoaded', () => {
  renderProjects();
  
  // Set active nav item
  const currentPath = window.location.pathname;
  if (currentPath === '/' || currentPath.endsWith('index.html')) {
    document.getElementById('home')?.classList.add('text-white', 'opacity-100');
  }
});

