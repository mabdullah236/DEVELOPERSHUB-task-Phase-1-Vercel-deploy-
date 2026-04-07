// document.addEventListener('DOMContentLoaded', () => {

//     // 1. Countdown Timer (index.html)
//     const countdownBoxes = document.querySelectorAll('.time-box span');
//     if (countdownBoxes.length === 4) {
//         // Example: Set countdown to 4 days, 13 hours, 34 mins, 56 secs from now
//         let days = parseInt(countdownBoxes[0].innerText) || 4;
//         let hours = parseInt(countdownBoxes[1].innerText) || 13;
//         let minutes = parseInt(countdownBoxes[2].innerText) || 34;
//         let seconds = parseInt(countdownBoxes[3].innerText) || 56;

//         let totalSeconds = days * 86400 + hours * 3600 + minutes * 60 + seconds;

//         const updateTimer = () => {
//             if (totalSeconds <= 0) return;
//             totalSeconds--;

//             const d = Math.floor(totalSeconds / 86400);
//             const h = Math.floor((totalSeconds % 86400) / 3600);
//             const m = Math.floor((totalSeconds % 3600) / 60);
//             const s = Math.floor(totalSeconds % 60);

//             countdownBoxes[0].innerText = d.toString().padStart(2, '0');
//             countdownBoxes[1].innerText = h.toString().padStart(2, '0');
//             countdownBoxes[2].innerText = m.toString().padStart(2, '0');
//             countdownBoxes[3].innerText = s.toString().padStart(2, '0');
//         };

//         setInterval(updateTimer, 1000);
//     }

//     // 2. Wishlist Toggle
//     const heartBtns = document.querySelectorAll('.btn-heart');
//     heartBtns.forEach(btn => {
//         btn.addEventListener('click', function(e) {
//             e.preventDefault();
//             const icon = this.querySelector('i');
//             if (icon.classList.contains('fa-regular')) {
//                 icon.classList.remove('fa-regular');
//                 icon.classList.add('fa-solid');
//                 icon.classList.add('text-danger');
//             } else {
//                 icon.classList.remove('fa-solid');
//                 icon.classList.remove('text-danger');
//                 icon.classList.add('fa-regular');
//             }
//         });
//     });

//     // 2b. Wishlist Toggle in save for later
//     // const saveLaterLinks = document.querySelectorAll('.save-later a, .cart-item-actions .btn-primary');
//     // saveLaterLinks.forEach(link => {
//     //     link.addEventListener('click', function(e) {
//     //         e.preventDefault();
//     //         const icon = this.querySelector('i');
//     //         if(icon) {
//     //              if (icon.classList.contains('fa-regular')) {
//     //                 icon.classList.remove('fa-regular');
//     //                 icon.classList.add('fa-solid');
//     //             } else {
//     //                 icon.classList.remove('fa-solid');
//     //                 icon.classList.add('fa-regular');
//     //             }
//     //         }
//     //        // toggle text 
//     //        if(this.innerText.includes('Save for later')) {
//     //            this.innerHTML = this.innerHTML.replace('Save for later', 'Saved');
//     //        } else if (this.innerText.includes('Saved')) {
//     //            this.innerHTML = this.innerHTML.replace('Saved', 'Save for later');
//     //        }
//     //     });
//     // });

//     // 3. Filter Accordion (product list/grid)
//     const filterHeaders = document.querySelectorAll('.filter-header');
//     filterHeaders.forEach(header => {
//         header.addEventListener('click', function() {
//             const icon = this.querySelector('i');
//             const targetList = this.nextElementSibling;
            
//             if (!targetList || !targetList.classList.contains('filter-list') && !targetList.classList.contains('range-slider')) return;
            
//             if (targetList.style.display === 'none') {
//                 targetList.style.display = '';
//                 if(this.nextElementSibling.nextElementSibling?.classList.contains('price-range-inputs')){
//                    this.nextElementSibling.nextElementSibling.style.display = '';
//                    this.nextElementSibling.nextElementSibling.nextElementSibling.style.display = ''; // Apply btn
//                 }
//                 if (icon) {
//                     icon.classList.remove('fa-chevron-down');
//                     icon.classList.add('fa-chevron-up');
//                 }
//             } else {
//                 targetList.style.display = 'none';
//                  if(this.nextElementSibling.nextElementSibling?.classList.contains('price-range-inputs')){
//                    this.nextElementSibling.nextElementSibling.style.display = 'none';
//                    this.nextElementSibling.nextElementSibling.nextElementSibling.style.display = 'none'; // Apply btn
//                 }
//                 if (icon) {
//                     icon.classList.remove('fa-chevron-up');
//                     icon.classList.add('fa-chevron-down');
//                 }
//             }
//         });
//     });

//     // 4. Product Gallery (product_detail.html)
//     const mainImg = document.querySelector('.main-image img');
//     const thumbs = document.querySelectorAll('.thumbnail-list .thumb');
    
//     if (mainImg && thumbs.length > 0) {
//         thumbs.forEach(thumb => {
//             thumb.addEventListener('click', function() {
//                 // Remove active class from all
//                 thumbs.forEach(t => t.classList.remove('active'));
//                 // Add active to clicked
//                 this.classList.add('active');
//                 // Change main image source
//                 const newSrc = this.querySelector('img').src;
//                 // typically higher res image would be swapped, using thumbnail src for demo
//                 mainImg.src = newSrc.replace('w=100', 'w=600'); 
//             });
//         });
//     }

//     // 5. Product Detail Tabs
//     const tabs = document.querySelectorAll('.detail-tabs .tab');
//     if (tabs.length > 0) {
//         // In a real app with separate tab contents, we'd toggle those too.
//         // For this template, just toggling active state visually.
//         tabs.forEach(tab => {
//             tab.addEventListener('click', function() {
//                 tabs.forEach(t => t.classList.remove('active'));
//                 this.classList.add('active');
//             });
//         });
//     }

//     // // 6. Cart Item Removal & Quantity Changes
//     // const removeBtns = document.querySelectorAll('.cart-item-actions .text-danger');
//     // removeBtns.forEach(btn => {
//     //     btn.addEventListener('click', function(e) {
//     //         e.preventDefault();
//     //         const cartItem = this.closest('.cart-item');
//     //         if (cartItem) {
//     //             cartItem.style.opacity = '0';
//     //             setTimeout(() => {
//     //                 cartItem.remove();
//     //                 updateCartTotal();
//     //             }, 300);
//     //         }
//     //     });
//     // });
    
//     // const removeAllBtn = document.querySelector('.btn-clear');
//     // if(removeAllBtn) {
//     //     removeAllBtn.addEventListener('click', function(e){
//     //         e.preventDefault();
//     //         const items = document.querySelectorAll('.cart-items-card .cart-item');
//     //         items.forEach(item => {
//     //             item.style.opacity = '0';
//     //             setTimeout(() => item.remove(), 300);
//     //         });
//     //         setTimeout(updateCartTotal, 350);
//     //     });
//     // }

//     const qtySelects = document.querySelectorAll('.qty-select');
//     qtySelects.forEach(select => {
//         select.addEventListener('change', function() {
//             // Re-calculate total in a real app, here we just simulate UI update
//             updateCartTotal();
//         });
//     });

//     function updateCartTotal() {
//         const titleBadge = document.querySelector('.page-title');
//         const items = document.querySelectorAll('.cart-items-card .cart-item');
//         if (titleBadge && items.length >= 0) {
//             titleBadge.innerText = `My cart (${items.length})`;
//         }
//     }
    
//     // Clear Filter chips
//     const clearFilterBtn = document.querySelector('.clear-filters');
//     const filterChips = document.querySelectorAll('.filter-chip');
//     if(clearFilterBtn) {
//         clearFilterBtn.addEventListener('click', () => {
//              filterChips.forEach(chip => chip.remove());
//              clearFilterBtn.remove();
//         });
//     }
    
//     filterChips.forEach(chip => {
//         chip.querySelector('i').addEventListener('click', function() {
//            this.parentElement.remove(); 
//         });
//     });

//     // ----------------------------------------------------------------------
//     // PHASE 2: Comprehensive Interactivity
//     // ----------------------------------------------------------------------

//     // Toast Notification System
//     const toastContainer = document.getElementById('toast-container');
//     function showToast(message, type = 'success') {
//         if (!toastContainer) return;

//         const toast = document.createElement('div');
//         toast.style.minWidth = '250px';
//         toast.style.padding = '12px 20px';
//         toast.style.borderRadius = '6px';
//         toast.style.color = '#fff';
//         toast.style.boxShadow = '0 4px 12px rgba(0,0,0,0.15)';
//         toast.style.display = 'flex';
//         toast.style.alignItems = 'center';
//         toast.style.justifyContent = 'space-between';
//         toast.style.opacity = '0';
//         toast.style.transform = 'translateY(20px)';
//         toast.style.transition = 'all 0.3s ease';
//         toast.style.zIndex = '9999';

//         if (type === 'success') {
//             toast.style.backgroundColor = '#00b517'; // success green
//             toast.innerHTML = `<span><i class="fa-solid fa-circle-check"></i> &nbsp; ${message}</span>`;
//         } else if (type === 'info') {
//             toast.style.backgroundColor = '#0d6efd'; // primary blue
//             toast.innerHTML = `<span><i class="fa-solid fa-circle-info"></i> &nbsp; ${message}</span>`;
//         }

//         const closeBtn = document.createElement('i');
//         closeBtn.className = 'fa-solid fa-xmark';
//         closeBtn.style.cursor = 'pointer';
//         closeBtn.style.opacity = '0.7';
//         closeBtn.onclick = () => {
//             toast.style.opacity = '0';
//             toast.style.transform = 'translateY(20px)';
//             setTimeout(() => toast.remove(), 300);
//         };
//         toast.appendChild(closeBtn);

//         toastContainer.appendChild(toast);

//         // Animate in
//         setTimeout(() => {
//             toast.style.opacity = '1';
//             toast.style.transform = 'translateY(0)';
//         }, 10);

//         // Auto remove
//         setTimeout(() => {
//             if (toast.parentElement) {
//                 toast.style.opacity = '0';
//                 toast.style.transform = 'translateY(20px)';
//                 setTimeout(() => { if (toast.parentElement) toast.remove(); }, 300);
//             }
//         }, 4000);
//     }

//     // Header Actions (base.html)
//     // const actionItems = document.querySelectorAll('.header-actions .action-item');
//     // actionItems.forEach(item => {
//     //     item.addEventListener('click', (e) => {
//     //         const aTag = item.querySelector('a');
//     //         if (aTag && aTag.getAttribute('href') && aTag.getAttribute('href') !== '#') {
//     //             // Valid link exists within action-item, let browser navigate naturally
//     //             return;
//     //         }
            
//     //         e.preventDefault();
//     //         const textSpan = item.querySelector('span');
//     //         const text = textSpan ? textSpan.innerText : 'Item';
//     //         showToast(`Opening ${text}...`, 'info');
//     //     });
//     // });

//     // Global Dead Link Handler (Catches all href="#")
//     document.addEventListener('click', function(e) {
//         const a = e.target.closest('a');
//         if (a && a.getAttribute('href') === '#') {
//             e.preventDefault();
//             const text = a.innerText.trim() || 'Demo Link';
//             showToast(`${text} clicked`, 'info');
//         }
//     });

//     // // Global Input Feedback (Checkboxes & Radios)
//     // document.addEventListener('change', function(e) {
//     //     if (e.target.type === 'checkbox' || e.target.type === 'radio') {
//     //         showToast('Filter option updated', 'success');
//     //     }
//     // });

//     // Mobile Menu Toggle (base.html)
//     const allCategoryToggle = document.querySelector('.all-category i.fa-bars');
//     const navLinksList = document.querySelector('.nav-links');
//     if (allCategoryToggle && navLinksList) {
//         allCategoryToggle.parentElement.addEventListener('click', () => {
//              // Basic mobile toggle simulation
//              if(window.innerWidth <= 768) {
//                  if(navLinksList.style.display === 'flex') {
//                      navLinksList.style.display = 'none';
//                  } else {
//                      navLinksList.style.display = 'flex';
//                      navLinksList.style.flexDirection = 'column';
//                      navLinksList.style.position = 'absolute';
//                      navLinksList.style.background = 'white';
//                      navLinksList.style.width = '100%';
//                      navLinksList.style.left = '0';
//                      navLinksList.style.top = '100%';
//                      navLinksList.style.padding = '15px';
//                      navLinksList.style.boxShadow = '0 4px 6px rgba(0,0,0,0.1)';
//                      navLinksList.style.zIndex = '1000';
//                  }
//              }
//         });
//     }

//     // Forms and Submissions
//     // 1. Send Inquiry / Quote
//     const quoteButtons = document.querySelectorAll('.quote-form .btn-primary, .overview-seller .btn-primary');
//     quoteButtons.forEach(btn => {
//         btn.addEventListener('click', (e) => {
//             e.preventDefault();
//             if(btn.innerText.includes('inquiry')) {
//                 showToast('Inquiry sent successfully to supplier!', 'success');
//             }
//         });
//     });

//     // 2. Newsletter Submit
//     const newsletterBtns = document.querySelectorAll('.newsletter-form .btn-primary');
//     newsletterBtns.forEach(btn => {
//         btn.addEventListener('click', (e) => {
//             e.preventDefault();
//             const input = btn.previousElementSibling.querySelector('input');
//             if(input && input.value) {
//                 showToast('Subscribed to newsletter!', 'success');
//                 input.value = '';
//             } else {
//                 showToast('Please enter an email address.', 'info');
//             }
//         });
//     });

//     // 3. User Login/Join (index.html)
//     // const joinLoginBtns = document.querySelectorAll('.user-widget .btn');
//     // joinLoginBtns.forEach(btn => {
//     //     btn.addEventListener('click', (e) => {
//     //         e.preventDefault();
//     //         showToast(`Navigating to ${btn.innerText}...`, 'info');
//     //     });
//     // });

//     // // pagination handles
//     // const pageControls = document.querySelectorAll('.page-controls button');
//     // pageControls.forEach(btn => {
//     //     btn.addEventListener('click', (e) => {
//     //         e.preventDefault();
//     //         // Ignore if it's an arrow icon
//     //         if(btn.querySelector('i')) return;
            
//     //         // Remove active from peers
//     //         const peers = btn.parentElement.querySelectorAll('button:not(:has(i))');
//     //         peers.forEach(p => p.classList.remove('active'));
            
//     //         btn.classList.add('active');
//     //         showToast(`Loading page ${btn.innerText}...`, 'info');
//     //     });
//     // });

//     // Apply Filter Button
//     const applyFilterBtns = document.querySelectorAll('.btn-apply');
//     applyFilterBtns.forEach(btn => {
//         btn.addEventListener('click', (e) => {
//             e.preventDefault();
//             showToast('Filters applied successfully.', 'success');
//         });
//     });

//     // Cart Interactions
//     const applyCouponBtns = document.querySelectorAll('.coupon-input .btn');
//     applyCouponBtns.forEach(btn => {
//         btn.addEventListener('click', (e) => {
//             e.preventDefault();
//             const input = btn.previousElementSibling;
//             if (input && input.value) {
//                 showToast(`Coupon "${input.value}" applied!`, 'success');
//             } else {
//                 showToast('Please enter a coupon code.', 'info');
//             }
//         });
//     });

//     const checkoutBtns = document.querySelectorAll('.btn-success.btn-lg');
//     checkoutBtns.forEach(btn => {
//         if(btn.innerText.includes('Checkout')) {
//             btn.addEventListener('click', (e) => {
//                 e.preventDefault();
//                 showToast('Proceeding to secure checkout...', 'info');
//             });
//         }
//     });

//     // Move to Cart (Saved Items)
// //     const moveBtns = document.querySelectorAll('.btn-move');
// //     moveBtns.forEach(btn => {
// //         btn.addEventListener('click', (e) => {
// //             e.preventDefault();
// //             const savedItem = btn.closest('.saved-item');
// //             if (savedItem) {
// //                 savedItem.style.opacity = '0';
// //                 savedItem.style.transform = 'scale(0.9)';
// //                 savedItem.style.transition = 'all 0.3s ease';
                
// //                 showToast('Item successfully moved to cart!', 'success');
                
// //                 setTimeout(() => {
// //                     savedItem.remove();
// //                     // Increment cart count visually
// //                     const titleBadge = document.querySelector('.page-title');
// //                     if(titleBadge) {
// //                         const currentCountMatch = titleBadge.innerText.match(/\((\d+)\)/);
// //                         if(currentCountMatch && currentCountMatch[1]) {
// //                             let count = parseInt(currentCountMatch[1]);
// //                             titleBadge.innerText = `My cart (${count + 1})`;
// //                         }
// //                     }
// //                 }, 300);
// //             }
// //         });
// //     });
// });
