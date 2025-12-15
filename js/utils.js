// Utility functions

export function sortMDByDate(posts = []) {
  return posts.sort(
    (a, b) =>
      new Date(b.publishDate).valueOf() -
      new Date(a.publishDate).valueOf()
  );
}

export function getFormattedDate(date) {
  const dateFormat = new Intl.DateTimeFormat("en-US", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
  return dateFormat.format(new Date(date));
}

export function setActiveNavItem(navbarActiveItemID) {
  const activeItemElement = document.getElementById(navbarActiveItemID);
  if (activeItemElement) {
    activeItemElement.classList.add("text-white", "opacity-100");
    activeItemElement.classList.remove("text-gray-400", "opacity-70");
  }
}

